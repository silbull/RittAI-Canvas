from pprint import pprint
import json, os, sys

JSON_INPUT_PATH = "datas/question_sentence/dataset_02.json"

# jsonから読み込み
with open(JSON_INPUT_PATH, "r", encoding="utf-8") as f:
    datas = json.load(f)

for data in datas:
    print(data["normalized"])
    print("\n")