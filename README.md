Disboardのフォーラムの新規投稿を通知するBOT
# forumannounce-bot

## 開発

```sh
docker compsoe build
BOT_TOKEN="<botのトークン>" SEND_CHANNEL_ID="<送信先のチャンネルID>" docker compose up
```

## デプロイ

- デプロイ先のサーバにsshで接続できるようにしておく
  - 接続先を `~/.ssh/config` に追加して、`ssh deployhost` のような形式で接続できる状態にしておく
- デプロイ先のサーバにDocker Engineをインストールする
  - https://docs.docker.com/engine/install/debian/
  - https://docs.docker.com/engine/install/linux-postinstall/ も忘れずに
- `deploy.sh` を作成する
  ```sh
  cp example.deploy.sh deploy.sh
  ```
- `deploy.sh` を任意のエディタで開き, 必要な情報を記載する
- デプロイ
  ```sh
  ./deploy.sh
  ```
