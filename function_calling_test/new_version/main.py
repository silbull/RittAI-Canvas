# %%
from __future__ import annotations
from dotenv import load_dotenv
import json, pprint
from pprint import pprint

import os, sys
sys.path.append(os.path.join(os.path.dirname("__file__"), '..'))

import openai

# %%
from classes.Completion import Completion
import parameter_extracter

# %%
# APIキーをファイルから読み込み，APIキー認証
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# %%
object_extracter = Completion(
    model="gpt-3.5-turbo",
    system_prompt="""I enter a math problem statement in Japanese. Please, extract the part object names and the type of object.""",
    funct={
        # 関数名と全体の説明
        "name": "part_objects_extract",
        "description": "This process extracts the part object names and the type of objects as an array",
        # 関数の詳細(引数)
        "parameters": {
            "type": "object",
            "properties": {
                # 第1引数
                "part_objects": {
                    # パーツオブジェクトのリスト(第1引数)
                    "type": "array",
                    "description": "An array of part object types and names",
                    "items": {
                        # リストの中身を辞書で定義
                        "type": "object",
                        "properties": {
                            "object_type": {
                                "type": "string",
                                "enum": ["Cube", "rectangular", "Segment", "Intersect", "Midpoint", "PerpendicularLine", "tetrahedron"],
                                "description": """Part objects include the following. Please select one type from the list in English such as "Cube", "Midpoint".
                                part_object_type = [
                                    ("立方体" → "Cube"),
                                    ("直方体" → "rectangular"),
                                    ("線分" → "Segment"),
                                    ("交点" → "Intersect"),
                                    ("中点" → "Midpoint"),
                                    ("垂線" → "PerpendicularLine"),
                                    ("四面体" → "tetrahedron"),
                                ]
                                Please, do NOT use symbols before their definitions. Use the order in which the definitions are given.
                                Bad example: ABCD-EFGF→BI→I
                                Good example: ABCD-EFGF→I→B"""
                            },
                            "object_name": {
                                "type": "string",
                                "description": "A name that identifies a shape. Restrict names to symbols only, such as ABCD-EFGH. If an obvious name does not exist in the problem statement, give an appropriate name, such as 'Perpendicular_A-BC'."
                            },
                        }
                    }
                }
            }
        }
    },
    examples=[
        (
            "1辺4の立方体ABCD-EFGH",
            "[{'object_name': 'ABCD-EFGH', 'object_type': 'Cube'}]"
        ),
        (
            "頂点Pから三角形ABCに垂線PHをおろす",
            "[{'object_name': 'PH', 'object_type': 'PerpendicularLine'}, {'object_name': 'H', 'object_type': 'Intersect'}]"
        ),
        (
            "AB = √3，AC=AD=BC=DB=4の四面体ABCDがある．また，辺CDの中点をMとする．頂点Aから三角形BCDに垂線AHを下ろしたとき，AHの長さを求めよ．",
            '[{"object_name": "ABCD", "object_type": "tetrahedron"},{"object_name": "M", "object_type": "Midpoint"},{"object_name": "AH", "object_type": "PerpendicularLine"},{"object_name": "H", "object_type": "Intersect"}'
        ),
        (
            "立体 PQRST-UVWX は、PQ = 35 cm、PR = 25 cm、PU = 45 cm の直方体である。頂点 R と頂点 U を結び、頂点 Q から線分 RU に引いた垂線と線分 RU との交点を I とする。線分 QI の長さは何 cm か。",
            '[{"object_name": "PQRST-UVWX", "object_type": "rectangular"},{"object_name": "RU", "object_type": "Segment"},{"object_name": "QI", "object_type": "PerpendicularLine"},{"object_name": "I", "object_type": "Intersect"}]'
        )
    ]
)

# %%
def main():
    # print("Q1")
    # pprint(object_extracter.create("立体ABCD-EFGHは，AB=40cm，AD=30cm，AE=50cmの直方体である．頂点Dと頂点Fを結び，頂点Bから線分DFに引いた垂線と線分DFとの交点をIとする．線分BIの長さは何cmか．"))
    # print("Q2")
    # pprint(object_extracter.create("直方体ABCD-EFGHにおいて，辺AB，AD，AEの長さをそれぞれa，b，cとする．また，頂点Aから直線FHにおろした垂線をALとする．"))
    return

if __name__ == '__main__':
    main()