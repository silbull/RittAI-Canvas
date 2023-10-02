# %%
from __future__ import annotations
from dotenv import load_dotenv
import json, pprint
from pprint import pprint

import os, sys
sys.path.append(os.path.join(os.path.dirname("__file__"), '..'))

import openai

# %%
# APIキーをファイルから読み込み，APIキー認証
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# %%
class Completion:
    def __init__(self,
        model = "gpt-3.5-turbo",
        system_prompt: str | None = None,
        funct: dict | None = None,
        examples: list[tuple[str|str]] | None = None,
    ):
        self.model = model
        self.system_prompt = system_prompt
        self.funct = funct
        self.examples = examples
    
    def create(self, input, p_flg=False):
        # 各種の引数を整形する
        # プロンプト類のリスト化
        messages = []
        if self.system_prompt is not None:
            messages.append({"role": "system", "content": self.system_prompt})
        if self.examples is not None:
            for example in self.examples:
                messages.append({"role": "user", "content": example[0]})
                messages.append({"role": "assistant","content": None,"function_call": {"name": self.funct["name"], "arguments": example[1]}})
        # function callingの設定 
        if self.funct is not None:
            functions = [self.funct]
            function_call = {"name": self.funct["name"]}
        # completion関数を実行
        messages.append({"role": "user", "content": input})
        print(f"START ChatCompletion ...", end="")
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            functions=functions,
            function_call=function_call,
            temperature=0,
        )
        print(f"FINISH")

        if p_flg: pprint(response)

        self.arguments = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])
        return self.arguments
    
    def print_datas(self):
        print(f"model: {self.model}")
        print(f"system_prompt: {self.system_prompt}")
        print("examples:")
        for example in self.examples:
            print(example)
        print(f"funct:")
        pprint(self.funct)