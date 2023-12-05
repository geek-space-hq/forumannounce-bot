#!/bin/sh

#
# つかいかた:
#   デプロイする場合, 引数なしで実行する
#     ./deploy.sh
#   その他の操作をする場合, 引数を指定して実行する
#     ./deploy.sh logs -f
#

# デプロイ先のホスト
#   ssh:// 以降にsshコマンドで指定できるのと同じ名前を指定する
DOCKER_HOST="ssh://raspberrypi.local"

# デプロイするコンテナのプレフィックス
#  とくにこだわりがなければこのままでOK
COMPOSE_PROJECT_NAME="forumannounce-bot"

# DiscordのBotのトークン
#   自分のBotのトークンを指定する
BOT_TOKEN=""

# 送信先チャンネルのチャンネルID
#   メッセージを送信したいチャンネルのIDを指定する
SEND_CHANNEL_ID=""

set -eu

docker_compose() {
  export DOCKER_HOST
  export COMPOSE_PROJECT_NAME
  export BOT_TOKEN
  export SEND_CHANNEL_ID
  docker compose "${@}"
}

args="${@:-""}"
if [ -n "${args}" ]; then
  docker_compose "${@}"
else
  docker_compose build
  docker_compose down
  docker_compose up -d --remove-orphans
fi
