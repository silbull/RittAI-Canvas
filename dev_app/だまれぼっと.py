"""メタボード用学習分析ツールの例"""
import os
from logging import DEBUG, INFO, WARNING
from pathlib import Path

from bookroll import BookRoll, BookRollSettings
from flask import Flask, render_template, session, request
from pylti.flask import lti

from util import common_init, get_writable_dir

import json
import openai

# ymlの構成を変える必要があるので，.envファイルの扱いはうまくいかない
# from dotenv import load_dotenv
# load_dotenv()
# openai.api_key = os.environ['OpenAI_APIkey']

app = Flask(__name__)
# app.debug = True

# ツール間で共通する処理を実行する
# Code Runの時はこの関数をコメントアウト
common_init(app)


# https://la.ait.kyushu-u.ac.jp/dev/metaboard/tools/ozaki/ にアクセスされた際に呼ばれる
@app.route('/')
@lti(request='session', app=app)  # LTIに対応させるデコレータ。すべての@app.routeに追加する
def index(lti):  # PyLTIから渡されるlti引数を追加する
    """ツールのトップページ。templates/index.htmlの内容を表示する"""
    return render_template('index.html')

# https://la.ait.kyushu-u.ac.jp/dev/metaboard/tools/ozaki/push/ にアクセスされた際に呼ばれる
@app.route('/push', methods = ["GET", "POST"])
@lti(request='session', app=app)
def pushed(lti):
    if request.method == "POST":
        json_request = request.get_json()
        input = json_request["input"]

        # output = input+"ここはpython"
        output = CreateAnswer(input)

        result = {"output": output}
        json_object = json.dumps(result, indent = 4)
        return(json_object)
    else:
        return("method == GET")

#OpenAI関係–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# これも無理
# with open("/dev/metaboard/tools/ozaki/api_key.txt") as f:
#     API_KEY = f.read()

API_KEY = 
openai.api_key = API_KEY

def CreateAnswer(user_msg):
    result = CreateCompletion_ATSUSHI(user_msg).choices[0].text

    return str(result)

def CreateCompletion(question):
    completion = openai.Completion.create(
        model="text-davinci-003", 
        prompt=question, 
        max_tokens=300,)
    return completion

course_info = """[{'_id': '62c6d23fbbee890ffec2fa67', 'id': '21255101', 'campus': 'ito', 'classroom': '_', 'degree': 2, 'department': '工学部', 'description': 'ディジタル的な処理手法によって信号を処理するディジタル信号処理技術は,高精度,高信頼性,処理の柔軟さなど,多くの利点をもっており,現在では幅広い分野で共通的な信号処理手法として利用されている.本講義では,ディジタル信号処理を理解し,活用するための基礎的な理論を学び,各分野での応用に備えさせる.以下に講義内容を示す.1.フーリエ変換,帯域制限信号と標本化定理(復習)\n2.離散時間信号(基本的な信号)と信号の基本的な演算\n3.離散時間信号のフーリエ変換と諸性質\n4.離散フーリエ変換対と高速フーリエ変換(FFT)\n5.離散時間システム(線形性,時不変性,因果性,インパルス応答,安定性)\n6.〃\n7.離散時間システムの入出力関係式,システムの結合\n8.差分方程式によって記述される離散時間システム\n9.離散時間システムの周波数応答,振幅特性,位相特性\n10.z変換による離散時間システムの解析-伝達関数,システムの結合,安定性条件など\n11.ディジタルフィルタの設計\n12.離散時間の不規則信号と定常確率過程,相関関数とパワースペクトル\nThe course "Digital signal processing" gives an introduction into discrete-time signals and systems.It covers methods for analyzing discrete-time signals and systems.It also provides how to design systems and to process signals for solving practical problems.1.Basics of digital signal processing:\nsampling theorem,and reconstruction of band limited signal\n2.Discrete-time signal\n3.Discrete-time Fourier transform and its propertie\n4.Discrete and fast Fourier transform\n5.Discrete-time system\n6.Linear time-invariant (LTI) systems and its properties,impluse response\n7.Difference equation ans system functions - I\n8.Difference equation ans system functions - II\n9.Frequency response of linear time-invariant system\n10.Z-transform,analysis of LTI systems in the z-domain\n11.Digital filter design\n12.Applications of digital signal processing:\ncorrelation Functions and power Spectrum estimation', 'etc': '・教室および曜日時限については,掲示される情報を必ず確認しておいてください.・他の授業と同様,Webによる履修登録を行ってください.・すべての授業に出席することが望まれますが,やむをえず欠席する場合は,事前または事後に必ず担当教員に連絡してください.・剽窃を含む不正行為には,厳しく対応します.・本学では,ハラスメントに関する相談や苦情の申出に対応するために,相談窓口・相談員を設置しています.ハラスメントの防止・対策について\nhttp://www.kyushu-u.ac.jp/university/harassment/\n・学習相談は随時受け付けます.担当教員に授業の際や電子メール等で相談してください.・授業に関わる活動に困難を感じた際には,できるだけ早く担当教員に相談してください.', 'grade': 3, 'keywords': 'ディジタル信号処理,フーリエ変換,離散時間信号,離散時間システム,離散フーリエ変換,差分方程式,周波数応答,z変換', 'moodle_course': None, 'name': 'ディジタル信号処理(A,C)', 'numbering_code': None, 'quaters': [1, 2], 'required': False, 'requirements': None, 'schedule': {'1': ['第1回ディジタル信号処理の概要', '◯', '演習も実施', ''], '2': ['第27回離散時間信号解析.\n(1)周期信号とフーリエ級数.\n(2)非周期信号とフーリエ変換.\n(3)連続時間信号の標本化.\n(4)離散時間信号とZ変換.\n(5)Z変換の性質,逆Z変換.\n(6)ここまでのまとめ', '◯', '演習も実施', ''], '3': ['第812回離散時間システム.\n(1)離散時間システム(線形時不変システム,インパルス応答,差分方程式).\n(2)離散時間システム(システム関数,周波数特性).\n(3)離散フーリエ変換.\n(4)高速フーリエ変換.\n(5)ここまでのまとめ', '◯', '演習も実施', ''], '4': ['第1315回フィルタ.\n(1)FIRディジタルフィルタの設計.\n(2)IIRディジタルフィルタの設計.\n(3)まとめ', '◯', '演習も実施', ''], 'No': ['進度・内容・行動目標', '講義', '演習・その他', '授業時間外学習']}, 'subject_category': None, 'subject_division': '専攻教育科目Specialized Education', 'target_major': '電気情報工学科(AC課程) / Department of Electrical Engineering and Computer Science', 'teachers': '島田敬士', 'timetable': '前期金曜日2時限', 'url': 'https://ku-portal.kyushu-u.ac.jp/campusweb/slbssbdr.do?value(risyunen)=2021&value(semekikn)=1&value(kougicd)=21255101&value(crclumcd)=', 'year': 2021, 'bow': {'ディジタル': 7, '手法': 2, '処理手法': 1, '信号': 11, '精度': 1, '信頼性': 1, '処理': 5, '利点': 1, '現在': 1, '共通': 1, '信号処理手法': 1, '信号処理': 3, '変換': 13, 'フーリエ変換': 4, '帯域制限信号': 1, '定理': 1, '標本化定理': 1, '復習': 1, '離散時間信号': 4, '演算': 1, '性質': 2, '諸性質': 1, '対': 1, '離散フーリエ変換対': 1, '高速フーリエ変換': 2, 'システム': 12, '離散時間システム': 9, '因果性': 1, '応答': 4, 'インパルス応答': 2, '安定性': 1, '関係式': 1, '入出力関係式': 1, '結合': 2, '方程式': 3, '差分方程式': 3, '周波数応答': 2, '特性': 3, '振幅特性': 1, '位相z変換': 1, '関数': 2, '解析伝達関数': 1, '条件': 1, '安定性条件': 1, 'フィルタ': 4, '設計': 3, '時間': 1, '離散時間': 1, '不規則信号': 1, '過程': 1, '確率過程': 1, '相関関数': 1, 'パワースペクトル"': 1, '離散フーリエ変換': 2, 'z変換': 3, 'ディジタル信号処理': 1, '概要': 1, '演習': 5, '実施': 4, '解析': 1, '離散時間信号解析': 1, '周期信号': 1, '級数': 1, 'フーリエ級数': 1, '非周期信号': 1, '連続時間信号': 1, '標本化': 1, '逆z変換': 1, 'まとめ': 3, 'iirディジタル': 1, '進度': 1, '目標': 1, '行動目標': 1, '専攻': 1, '時間外学習専攻': 1}}]"""
def CreateCompletion_ATSUSHI(question):
    completion = openai.Completion.create(
        model="text-davinci-003", 
        prompt=course_info + question, 
        max_tokens=300,)
    return completion

# print(CreateCompletion("AIとは何か．簡単に説明してください．").choices[0].text)
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

#syllabusの情報を読む––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# JSONファイルがあるファイルパス !!LALA環境下では注意!!
# 無理でした
# print("READ Start")
# file_path = '/dev/metaboard/tools/ozaki/static/data/syllabi.json'

# # Open関数でファイルをロード
# with open(file_path) as f:
#     data = json.loads(f.read())

# print("READ Finished")
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

#json検索関数––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#シラバスのJSONのリスト"l"から，"k" == "v" の条件に合うシラバスを検索し，リストとして返す．
#"p_flg"がTrueの場合は検索結果をprintする．
def Search_Lecture_JSON(l, k, v, p_flg=0):
    results = list(filter(lambda item : item[k] == v, l))
    if (p_flg):
        print("【結果】", len(results), "件ヒットしました．")
        print(results)

    return results
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# json_21533008 = Search_Lecture_JSON(data, "id", "21533008", 0)
# print(json_21533008)