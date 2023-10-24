# Texto3D / dev_miyawaki
フロントの実装

## 実行方法

#### 1. Venvによる仮想環境の作成
1. VSCodeでコマンドパレットを開き，`Python: Create Environment`を選択．
2. `Venv`を選択
3. Pythonのバージョンを選択．自身の環境に入っているバージョンを選択することができます．3.10での動作は確認済みです．3.10以上を推奨します．
4. 依存環境を選択．ここでは，`requirements.txt`を選択してください
5. 仮装環境のアクティベート

・Linux/macOSの場合
```
source .venv/bin/activate
```
・Windowsの場合
```
.venv\Scripts\activate
```
#### 2. ポートの立ち上げ
ターミナルで以下の操作を行ってください．
1. dev_appディレクトリに移動
```zsh:
cd dev app
```
2. ポートの立ち上げ
```zsh:
python backend/app/app.py
```
3. 表示されたURLにアクセス



## 注意点

#### 各自用意が必要な部分

#### 1.OpenAI API Key

OpenAI API 関係のプログラムを実行するためにはAPIキーが必要です．
フォルダ下のどこでも良いので`.env`ファイルを作成し，APIキーを環境変数として登録してください．

```.env:.env
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
#### 2. Google Vision API Key

OCR機能を使うためにはGoogle Vision APIのキーが必要です．
[こちら](https://self-development.info/python%E3%81%A7google-cloud-vision-api%E3%82%92%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/　)の記事を参考にGoogle Cloud Platformのアカウントを作成し，Vision APIを有効化してください．秘密鍵(jsonファイル)のダウンロードまで終わったら，`1`で作成した`.env`ファイルに以下のように追記してください．("xxxx"の部分は各自の秘密鍵の内容です)

```.env:.env
GOOGLE_APPLICATION_CREDENTIALS = '{
    "type": "xxxx"
    "project_id": "xxxx",
    "private_key_id": "xxxx",
    "private_key": "xxxx",
    "client_email": "xxxx",
    "client_id": "xxxx",
    "auth_uri": "xxxx",
    "token_uri": "xxxx",
    "auth_provider_x509_cert_url": "xxxx",
    "client_x509_cert_url": "xxxx",
    "universe_domain": "xxxx"
}'
```
