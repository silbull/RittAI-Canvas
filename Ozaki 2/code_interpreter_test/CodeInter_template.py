# %%
import json, pprint
from codeinterpreterapi import CodeInterpreterSession, File
from dotenv import load_dotenv

# %%
import os, sys
sys.path.append(os.path.join(os.path.dirname("__file__"), '..'))

# %%
# APIキーをファイルから読み込み，APIキー認証
load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

# %%
async def MakeCompletion(prompt:str, file:list=[]):
    async with CodeInterpreterSession(
        openai_api_key = API_KEY, 
        model = "gpt-4"
    ) as session:
        
        response = await session.generate_response(
            user_msg = prompt,
            files = file,
            detailed_error = True,
        )

        response.show()
        return response

# %%
# ファイルパス群
JSON_INPUT_PATH = "datas/question_sentence/dataset_01.json"

# %%
# jsonから読み込み
with open(JSON_INPUT_PATH, "r", encoding="utf-8") as f:
    question_json_list = json.load(f)

if __name__ == "__main__":
    import asyncio
    asyncio.run(MakeCompletion("以下の説明から図を表現するためのGeoGebra Scriptを書けますか？"))
