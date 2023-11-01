from flask import Flask, render_template, request, jsonify
import json, pprint
import sys, os
from pathlib import Path
from PIL import Image
from google.cloud import vision
from google.oauth2 import service_account
from dotenv import load_dotenv
from controllers.MakeScript import ChatCompletion
import time



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

# 画像を受け取り，OCRを行なってテキストを返す
@app.route('/run_ocr', methods = ["GET", "POST"])
def RunOCR():
    if request.method == "POST":
        # 身元証明書のjsonファイルを読み込む
        load_dotenv()
        google_credentials = os.getenv('GOOGLE_CREDENTIALS')
        credentials = service_account.Credentials.from_service_account_info(json.loads(google_credentials))
        
        # 画像解析メソッドを提供するクライアントを作成
        client = vision.ImageAnnotatorClient(credentials=credentials)
        
        # jpg, jpegはなぜか画像が回転してしまうので，回転情報を取得して元の向きに戻し，pngに変換してOCRを行う
        if request.files["image"].filename.endswith(".jpeg") or request.files["image"].filename.endswith(".jpg"):
            image = Image.open(request.files["image"])
             # EXIFデータから回転情報を取得
            exif_data = image.getexif()
            orientation_tag = 274  # 'Orientation'タグのID

            if exif_data and orientation_tag in exif_data:
                orientation = exif_data[orientation_tag]

                rotate_values = {
                    3: 180,
                    6: 270,
                    8: 90
                }

                # 画像を適切に回転
                if orientation in rotate_values:
                    image = image.rotate(rotate_values[orientation], expand=True)
            image.save("input.png") # 一時的にpngに変換して保存

            with open("input.png", "rb") as image_file:
                content = image_file.read()

            image = vision.Image(content=content)
            text = client.document_text_detection(image=image).full_text_annotation.text # OCRを実行
            os.remove("input.png") # 一時的に保存したpngを削除

        else: # jpeg, jpg以外の場合
            file = request.files["image"]
            content = file.read()
            image = vision.Image(content=content)
            text = client.document_text_detection(image=image).full_text_annotation.text
        
        # 改行文字，空白文字を削除
        text = text.replace("\n", "").replace(" ", "")

        return jsonify({"text": text})
    else:
        return("method == GET")


# 問題文を受け取ってopenai.ChatCompletion.creatに渡す
@app.route('/push2gpt', methods = ["GET", "POST"])
def Push2GPT():
    if request.method == "POST":
        input = request.get_json()["input"]

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

        output = res["choices"][0]["message"]["content"]

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
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=True)
