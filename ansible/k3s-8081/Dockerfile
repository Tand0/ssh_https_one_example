FROM python:3.13-slim

# 環境変数の設定 (Pythonのpycファイルを作成しない、ログをバッファリングしない)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリの設定
WORKDIR /app

# ライブラリのインストール
RUN pip install fastapi uvicorn

# アプリケーションのコードをコピー
COPY server_fast.py .

# 実行コマンド
CMD ["python", "server_fast.py", "8081", "efg"]

