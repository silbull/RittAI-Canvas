# Texto3D / dev_Ozaki
尾崎が色々試行錯誤したものの残骸達です．__
主にGINZAを用いた言語解析，opemai apiによるGPTとのプロンプトのテスト結果があります．

## フォルダ構成

フォルダ構成は以下のようになっています．(記入日23.8.29)

### .codebox
> Code Interpreter API実行時に作られるフォルダなので，気にしなくてよいです．
### .vscode
> vscode用の設定ファイルなので，気にしなくてよいです．
### code_interpreter_test
> Code Interpreter APIを使ってみましたが，日本語の精度が絶望的に悪くて，断念しました．
### datas
##### commands
> GeoGebra 3Dで使えるコマンドをまとめたjosnがあります．
##### graphs
> GINZAによる係り受け解析を有向グラフで可視化したものです．
##### question_sentence
> 数学問題文があります．
##### tioken
> GINZAで数学特有単語を洗い出した結果です．
### GINZA_test
> GINZAで係り受けや重要語抽出など，色々やってみたものです．
### miyawaki_prompt
> 宮脇くんが試験してくれたGPT向けプロンプトをAPIで実装しています．
### OpenAI_test
> 過去にOpenAI APIを試験的に使ってみた残骸です．
### others
> 文字通りその他．

## 注意点

#### OpenAI API Keyについて

OpenAI API 関係のプログラムを実行するためにはAPIキーが必要です．
フォルダ下のどこでも良いので`.env`ファイルを作成し，APIキーを環境変数として登録してください．

```.env
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
