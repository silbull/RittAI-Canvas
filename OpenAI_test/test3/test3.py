import openai

#APIキーをファイルから読み込み，APIキー認証
f1 = open("GPT_API_key.txt", 'r', encoding='UTF-8')
key = f1.read()
f1.close
openai.api_key = key

#インストラクションファイルを読み込む
f2 = open('test3/initial_instructions3.txt', 'r', encoding='UTF-8')
initial_instructions = f2.read()
f2.close

completion = openai.Completion.create(
    model="text-davinci-003", 
    prompt=initial_instructions, 
    max_tokens=300
)

print(completion)
print("【回答】", completion.choices[0].text)

# talk_log = [
#             {"role": "system", "content": initial_instructions},
#            ]

# def GetAnswer(question, talk_log):
#     talk_log.append({"role": "user", "content": question})

#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = talk_log,
#     )

#     # print("【レスポンス】", response)
#     print("【アンサー】", response["choices"][0]["message"]["content"])
#     print("")

#     talk_log.append(response["choices"][0]["message"])

# # print(talk_log)

# while True:
#     input_question = input("【質問】")
#     print("回答生成中……")
#     GetAnswer(input_question, talk_log)