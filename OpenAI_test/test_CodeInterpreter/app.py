# %%
from dotenv import load_dotenv
import os, sys
import openai

import json, ndjson, pprint

from time import sleep
import logging
import datetime

from codeinterpreterapi import CodeInterpreterSession, File

# %%
# APIキーをファイルから読み込み，APIキー認証
load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

# %%
prompt_jap = """以下の文章に説明を補足して，文章を拡張してください．250〜270文字程度の文章を生成してください．
文字数を数える際はlen関数などを使用してください．
生成した文章と文字数を出力してください．
'機械学習は、データに基づいて訓練されたアルゴリズムに基づく人工知能の一形態である。'
"""

prompt_eng = """Please, revise next sentence so that the total word counts of new sentence could be about 50 words by calculating length of sentence.
And then, show new sentence, num of total word count.

'Machine learning is a form of artificial intelligence based on algorithms that are trained on data.'
"""

prompt_BoW = """Please, revise next sentence so that the total of Bow of new sentence could be about 50 by calculating BoW.
When calculating BoW, please eliminate common words and sumbols like period from new sentence. The input file 'test_CodeInterpreter/stopwords_eng.txt' has list of stopwords.
And then, show new sentence, num of total bow and BoW json.

'Machine learning is a form of artificial intelligence based on algorithms that are trained on data.'
"""

prompt = """jsonファイルは九州大学の3つの講義のシラバスです．すべての講義は8回分の構成です．
"Data"の中の"objectives_Jap"に授業全体の概要が書かれています．
"Data"の中の"schedule"に各授業回ごとの内容が書かれています．
これらの情報をもとにして，各授業回間の類似度を計算し，ヒートマップを作成してください．
24*24の大きさの対称行列と24*24の大きさのヒートマップを出力として期待します．
"""


file = [
    # File.from_path("test_CodeInterpreter/stopwords_eng.txt"),
    File.from_path("test_CodeInterpreter/syllabi_schedules.json"),
]

# %%
async def main():
    API_KEY = "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"
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

# %%
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
