import discord
from discord.ext import commands
from discord import app_commands
import os
import json

BOT_TOKEN=os.environ['forumannouce-bot-API-TOKEN']
SETTING_JSON="settings.json"
intents = discord.Intents.default()
intents.members = True # メンバー管理の権限
intents.message_content = True # メッセージの内容を取得する権限

bot = discord.Client(intents=intents) # 権限を設定
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    print("login!")
    await tree.sync()#スラッシュコマンドを同期

async def on_thread_create(thread: discord.Thread):
    if(thread.parent.type=="forum"): #forumの新規ポストを監視する
        print("forum create!!")

@tree.command(name="frgs",description="フォーラム通知を流すチャンネルをこのチャンネルに設定します")
async def test_command(interaction: discord.Interaction):
    with open(SETTING_JSON,'r')as f:
        settings=json.load(f)
    print(settings)
    settings['send_messagechannel_ID']=interaction.channel_id
    with open(SETTING_JSON,'w')as f:
        json.dump(settings,f)
    await interaction.response.send_message(interaction.channel_id,ephemeral=True)
bot.run(BOT_TOKEN)