# Texto3D / dev_Ozaki
尾崎が色々試行錯誤したものの残骸達です．__
主にGINZAを用いた言語解析，opemai apiによるGPTとのプロンプトのテスト結果があります．

## フォルダ構成

フォルダ構成は以下のようになっています．(記入日23.8.29)

#### .codebox
Code Interpreter API実行時に作られるフォルダなので，気にしなくて良いです．
#### .vscode
#### code_interpreter_test
#### datas
#### GINZA_test
#### miyawaki_prompt
#### OpenAI_test
#### others

## 注意点

#### OpenAI API Keyについて

OpenAI API 関係のプログラムを実行するためにはAPIキーが必要です．
フォルダ下のどこでも良いので`.env`ファイルを作成し，APIキーを環境変数として登録してください．

```.env
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
