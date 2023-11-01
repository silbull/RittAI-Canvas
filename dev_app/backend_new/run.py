# Webサーバを立ち上げる際に実行するファイル．エンドポイント．
from app.app import app

if __name__ == "__main__":
    app.run()
