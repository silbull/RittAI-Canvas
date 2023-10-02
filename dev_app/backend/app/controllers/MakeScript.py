# %%
import json, ndjson, pprint
from dotenv import load_dotenv

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