# %%
import json, ndjson
from dotenv import load_dotenv
from pprint import pprint

import openai

from time import sleep
import logging
import datetime

# %%
import os, sys
sys.path.append(os.path.join(os.path.dirname("__file__"), '..'))

# %%
# APIキーをファイルから読み込み，APIキー認証
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# %%
# 処理時間を計測するため、loggerのフォーマット設定しています
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format = '%(asctime)s [%(levelname)s] %(filename)s, lines %(lineno)d. %(message)s'
formatter = logging.Formatter(format, '%Y-%m-%d %H:%M:%S')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# %%
# トークログ(プロンプト)のバックアップログを取る関数
def AddBackUpLog_gptPrompt(prompt:dict):
    dt_now = datetime.datetime.now()
    BACKUP_LOG_PATH = f"./backend/app/controllers/gpt_log/openai.ChatCompletion.create_{dt_now.year}-{dt_now.month}-{dt_now.day}.ndjson"
    with open(BACKUP_LOG_PATH, 'a') as f:
        writer = ndjson.writer(f, ensure_ascii=False)
        writer.writerow(prompt)

# %%
# リトライ付きChatCompletion
def ChatCompletion(
        messages:list, 
        model:str = "gpt-4", 
        max_token:int = 4000
):
    for message in messages:
        AddBackUpLog_gptPrompt(message) # GPT入力/出力のログを取る
    retry_interval = 2
    tries = 4
    for num_try in range(1, tries+1):
        try:
            print(f"START ChatCompletion.create Contents ... ", end="")
            response = openai.ChatCompletion.create(
                model = model,
                messages = messages,
                max_tokens = max_token
            )
            print(f"FINISH ChatCompletion.create")
            AddBackUpLog_gptPrompt(response["choices"][0]["message"]) # GPT入力/出力のログを取る
            break
        except:
            print(f"ChatCompletion.create ERROR")
            if num_try == tries:
                raise
            sleep(retry_interval)
            logger.info(f'リトライ回数:{num_try}回目')
            continue
    return response

# %%
def text2GGB_direct(input):
    system_prompt = """I enter a math problem statement in Japanese. Please, generate a GeoGebra Script to visualize it. 
    Always abide by the following 2 rules:
    1. if the exact coordinates are to be determined from the length, this can be done by solving the following equations.
    Example
    A(Xa,Ya),B(Xb,Yb),a=BC,b=AC, C = (x, y)
    Then
    (x-Xa)^2+(y-Ya)^2 = a^2
    (x-Xb)^2+(y-Yb)^2 = b^2
    2. Please do not leave any comments, return only geogebra script in code space.

    Also,The following functions must also be used for specific Japanese words.
    "線分": Segment()
    "中点": Midpoint(Object, Object)
    "垂線": PerpendicularLine()
    "角形": Polygon()
    "円錐": Cone(Circle, Height)
    "円柱": Cylinder(Circle, Height)
    "交点": Intersect(Object, Object)
    "1回転": Surface(Object, 360, Line)"""

    ex_q1 = "立体ABCD-EFGHは，AB=40cm，AD=30cm，AE=50cmの直方体である．頂点Dと頂点Fを結び，頂点Bから線分DFに引いた垂線と線分DFとの交点をIとする．線分BIの長さは何cmか．"
    ex_a1 = """A = (0, 0, 0)
    B = (40, 0, 0)
    C = (40, 30, 0)
    D = (0, 30, 0)
    E = (0, 0, 50)
    F = (40, 0, 50)
    G = (40, 30, 50)
    H = (0, 30, 50)
    Segment(A, B)
    Segment(B, C)
    Segment(C, D)
    Segment(D, A)
    Segment(E, F)
    Segment(F, G)
    Segment(G, H)
    Segment(H, E)
    Segment(A, E)
    Segment(B, F)
    Segment(C, G)
    Segment(D, H)
    Segment(D, F)
    I = PerpendicularLine(B, Segment(D, F))"""
    ex_q2 = "AB=5 cm，BC=6 cm，AD=3 cm，∠C=∠D=90°の台形 ABCD を，辺 DC を軸として 1回転させてできる立体"
    ex_a2 = """C = (0,0,0)
    B = (6,0,0)
    A = (3,0,4)
    D = (0,0,4)
    a = Segment(A, B)
    b = Segment(B, C)
    c = Segment(C, D)
    d = Segment(D, A)
    q1 = Polygon(A, B, C, D)
    e = Surface(q1, 360, c)"""

    messages = [
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":ex_q1},
        {"role":"assistant", "content":ex_a1},
        {"role":"user", "content":ex_q2},
        {"role":"assistant", "content":ex_a2},
    ]

    input_question = input
    messages.append({"role":"user", "content":input_question})

    res = ChatCompletion(
        messages, 
        #  model = "gpt-3.5-turbo-16k",
        model = "gpt-4",
        max_token = 4000
    )
    pprint(res)
    output = res["choices"][0]["message"]["content"]
    return output