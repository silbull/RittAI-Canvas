# %%
import json, pprint

# %%
import os, sys
sys.path.append(os.path.join(os.path.dirname("__file__"), '..'))


# %%
# ファイルパス群
JSON_INPUT_PATH = "datas/question_sentence/dataset_01.json"

# %%
# jsonから読み込み
with open(JSON_INPUT_PATH, "r", encoding="utf-8") as f:
    question_json_list = json.load(f)

if __name__ == "__main__":
    ans = ""
    for sentence in question_json_list[0]["answer"]:
        ans += sentence + "\n"
    
    print(ans)
