# Python 3.11.8をベースイメージとして使用
FROM python:3.11.8

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なPythonライブラリをファイルに記述
COPY requirements.txt ./
# requirements.txtに記載されたライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# Dockerfileと同じディレクトリにあるファイルをコンテナ内の作業ディレクトリにコピー
COPY . .


