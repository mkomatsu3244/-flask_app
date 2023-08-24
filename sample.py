#必要なモジュールのインポート
from flask import Flask

#　Flask をインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあった時の処理
@app.route("/")
def hello():
    return "Hello World!"

# エントリーポイント
if __name__ == "__main__": # sample.pyが直接実行された場合という理解でOK。そのときにappが実行される
    app.run()

