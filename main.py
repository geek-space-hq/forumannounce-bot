import discord
from discord.ext import commands
from discord import app_commands
import os

BOT_TOKEN=os.environ['forumannouce-bot-API-TOKEN']

intents = discord.Intents.default()
intents.members = True # メンバー管理の権限
intents.message_content = True # メッセージの内容を取得する権限


# Botをインスタンス化
bot = commands.Bot(
    command_prefix="$", # $コマンド名　でコマンドを実行できるようになる
    case_insensitive=True, # コマンドの大文字小文字を区別しない ($hello も $Hello も同じ!)
    intents=intents # 権限を設定
)


@bot.event
async def on_ready():
    print("login!")
    
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    await message.reply(message.content)

bot.run(BOT_TOKEN)