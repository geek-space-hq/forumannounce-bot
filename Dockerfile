# ベースとなるDockerイメージ指定
FROM python:3.12.0-slim-bookworm

RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係のリストをコピー
COPY requirements.txt requirements.txt

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . .

# ストップシグナル
STOPSIGNAL SIGINT

# アプリケーションを起動
CMD ["python3", "main.py"]
