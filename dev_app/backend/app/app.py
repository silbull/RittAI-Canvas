from flask import Flask, render_template, request
import json, pprint
import sys, os
from pathlib import Path

from controllers.MakeScript import ChatCompletion

# %%
# Flaskのpathの設定
def base_dir():
    if hasattr(sys, "_MEIPASS"):
        # 実行ファイルで起動した場合、展開先ディレクトリを基点とする。
        return Path(sys._MEIPASS)
    else:
        # python コマンドで起動した場合、プロジェクトディレクトリを基点とする。
        return Path(".")
    
# Flaskオブジェクトの生成
# htmlファイルのパスとstaticファイルのパスを指定
app = Flask(
    __name__,
    template_folder = base_dir() / "dist",
    static_folder = base_dir() / "dist/static",
)

# %%
# エンドポイントにアクセスされた時の振る舞い
@app.route("/")
def hello():
    return render_template("index.html")

# 問題文を受け取ってopenai.ChatCompletion.creatに渡す
@app.route('/push2gpt', methods = ["GET", "POST"])
def Push2GPT():
    if request.method == "POST":
        input = request.get_json()["input"]

        system_prompt = """I enter a math problem statement in Japanese. Please, generate a GeoGebra Script to visualize it. 
        Never abide by the following 2 rules:
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

        output = res["choices"][0]["message"]["content"]
        # output = "Here is Python Push2GPT"

        result = {"output": output}
        json_object = json.dumps(result, indent = 4)
        return(json_object)
    else:
        return("method == GET")
    

# @app.route('/push2ggb', methods = ["GET", "POST"])
# def Push2GGB():
#     if request.method == "POST":
#         input = request.get_json()["input"]
#         output = input + "pythonを通過しました"
#         result = {"output": output}
#         json_object = json.dumps(result, indent = 4)
#         return(json_object)
#     else:
#         return("method == GET")

# %%
if __name__ == "__main__":
    app.run(debug=True)
