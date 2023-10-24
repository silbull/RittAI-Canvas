# %%
from __future__ import annotations
from dotenv import load_dotenv
import json, pprint
from pprint import pprint

import os, sys
sys.path.append(os.path.join(os.path.dirname("__file__"), '..'))

import openai

# %%
# オブジェクト抽出機を part_objects_extracter.py からインポート
from controllers.text2GGBscript.part_objects_extracter import part_object_extracter
# パラメータ抽出機のインスタンスを作成する関数群を parameter_extracter.py からインポート
import controllers.text2GGBscript.parameter_extracter as parameter_extracter
# スクリプト生成機を parameter_extracter.py からインポート
import controllers.text2GGBscript.GGBscript_maker as GGBscript_maker

# %%
# APIキーをファイルから読み込み，APIキー認証
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# %%
# パラメータ抽出機 文字列→関数 の変換用
instance_creator_functs = {
    "rectangular": parameter_extracter.rectangular,
    "Cube": parameter_extracter.Cube,
    "Segment": parameter_extracter.Segment,
    "Intersect": parameter_extracter.Intersect,
    "Midpoint": parameter_extracter.Midpoint,
    "PerpendicularLine": parameter_extracter.PerpendicularLine,
    "tetrahedron": parameter_extracter.tetrahedron,
}

# スクリプト生成機 文字列→関数 の変換用
script_maker_functs = {
    "rectangular": GGBscript_maker.rectangular,
    "Cube": GGBscript_maker.Cube,
    "Segment": GGBscript_maker.Segment,
    "Intersect": GGBscript_maker.Intersect,
    "Midpoint": GGBscript_maker.Midpoint,
    "PerpendicularLine": GGBscript_maker.PerpendicularLine,
    "tetrahedron": GGBscript_maker.tetrahedron,
}

# %%
def text2GGBscript(question_sentence):
    print("Q1")
    # 問題文の入力
    # question_sentence = "立体ABCD-EFGHは，AB=40cm，AD=30cm，AE=50cmの直方体である．頂点Dと頂点Fを結び，頂点Bから線分DFに引いた垂線と線分DFとの交点をIとする．線分BIの長さは何cmか．"
    
    # オブジェクト抽出機を実行して，オブジェクトのリストを抽出
    part_objects = part_object_extracter.create(question_sentence, p_flg=True)

    output = ""
    # パラメータ抽出機とスクリプト生成機を実行
    for part_object in part_objects:
        # パラメータを抽出する
        # パラメータ抽出機インスタンスを作成する関数を選定
        instance_create_func = instance_creator_functs[part_object["object_type"]]
        # インスタンス作成関数を実行
        parameter_extracter = instance_create_func(part_object["object_name"])
        # パラメータ抽出を実行し辞書に保存
        parameter = (parameter_extracter.create(question_sentence, p_flg=True))
        part_object["parameters"] = parameter

        # GGBScriptを生成する
        # スクリプト生成機を作成する関数を選定
        script_maker_func = script_maker_functs[part_object["object_type"]]
        # スクリプト生成関数を実行し辞書に保存
        GGBscript = script_maker_func(part_object)
        part_object["GGBscript"] = GGBscript
        # 最終的なアウトプットを作る
        output += GGBscript

    print("パラメータとスクリプトのjson")
    pprint(part_objects)
    print("スクリプト生成機の最終結果")
    print(output)
    return output

if __name__ == '__main__':
    text2GGBscript("問題文をここに入力")