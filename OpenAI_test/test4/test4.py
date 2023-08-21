from dotenv import load_dotenv
import os
import openai
import json

#APIキーをファイルから読み込み，APIキー認証–––––––––
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']
#–––––––––––––––––––––––––––––––––––––––––––––

#シラバス情報のjsonファイルを読み込む–––––––––––––––––––
print("READ Start")

file_path = 'data/syllabi.json'
with open(file_path) as f:
    data = json.loads(f.read())

print("READ Finished")
#––––––––––––––––––––––––––––––––––––––––––––––––––

#授業検索–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#シラバスのJSONのリスト"l"から，"k" == "v" の条件に合うシラバスを検索し，リストとして返す．
#"p_flg"がTrueの場合は検索結果をprintする．
def Search_Lecture_JSON(l, k, v, p_flg=0):
    results = list(filter(lambda item : item[k] == v, l))
    if (p_flg):
        print("【結果】", len(results), "件ヒットしました．")
        print(results)

    return results
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

#指定した授業のシラバスをプロンプトにセットする関数–––––––––––––––––––––––
def SetSyllabus(l, k, v):
    initial_instructions = "大学の授業に関するシラバスデータを，JSON形式で以下に示しています．" + str(Search_Lecture_JSON(l, k, v)[0])
    talk_log.append({"role": "system", "content": initial_instructions})
#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

#トークログに従って対話する関数–––––––––––––––––––––––––––––
def GetAnswer(question, talk_log):
    talk_log.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = talk_log,
    )

    # print("【レスポンス】", response)
    print("【アンサー】", response["choices"][0]["message"]["content"])
    print("")

    talk_log.append(response["choices"][0]["message"])
#––––––––––––––––––––––––––––––––––––––––––––––––––––––

talk_log = []

SetSyllabus(data, "teachers", "島田敬士")

while True:
    input_question = input("【質問】")
    print("回答生成中……")
    GetAnswer(input_question, talk_log)