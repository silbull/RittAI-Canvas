from flask import Flask, render_template, request
import json, pprint
import sys, os
from pathlib import Path

# %
from controllers.MakeScript import ChatCompletion
from controllers.text2GGBscript.main import text2GGBscript

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
        # 問題文からGGBスクリプトを生成
        output = text2GGBscript(input)
        # フロント側にoutputを送信
        result = {"output": output}
        json_object = json.dumps(result, indent = 4)
        return(json_object)
    else:
        return("method == GET")

# %%
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)
