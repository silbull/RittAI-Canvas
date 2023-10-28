# 開発手順

## 前提

`dev_app/`ディレクトリをアプリプロジェクトのルートディレクトリとする．

## Vueプロジェクトの新規作成方法について

npmでVueプロジェクトを作るのではなく，Vue CLIを使ってプロジェクトを新規作成した．

#### 従来手法

```zsh:
cd ~/
npm create vue@latest

...プロジェクト名やオプションを選択

cd <プロジェクト名>
npm install
```

#### 新手法

```zsh:
cd ~/
vue create <プロジェクト名>
```


## フロントエンドの開発について

バックエンドに関係しないフロントエンドの開発はnode.jsを用いたdevサーバを立ておくことで，いちいちコンパイルする必要がなくなる．
```zsh:
cd frontend
npm run serve
```
#### ただし，エラー発見機が優秀すぎて，細かいwarningなどもいちいち吐いてくる(超めんどくさい)．そこで，以下の対策法により一部のエラーを無視するように設定してある．

1. `package.json`に`"rules": {"no-unused-vars": "off"}`を記載
2. `.vue`ファイルのscriptタグに`/* eslint-disable */`をコメントアウトとして記載

## コンパイルとFlaskサーバの立ち上げについて

### 1. フロントエンドのコンパイル

`frontend`ディレクトリにて.vue系ファイルのコンパイルを実行し，.html .js .cssファイルを作成する．

```zsh:
cd frontend
npm run build
```

出力されるファイルは`~/backend/app/dist`に纏まるように設定してある．出力先の設定は`~/frontend/vue.config.js`に追記した．

### 2. Flaskの実行

`~/backend/run.py`あるいは`~/backend/app/app.py`を実行することで，Flaskサーバが起動する．後者はデバッグモードで起動する．  
> **23/9/8現在，後者のデバッグモードでの起動にしか対応していません．**

```zsh:
cd backend
python run.py 
```

あるいは
```zsh:
cd dev_app
python backend/app/app.py 
```

### 3. サーバにアクセス
おそらく`http://127.0.0.1:5000`にホストが立つので，ブラウザでアクセスする．