import discord
from discord.ext import commands
from discord import app_commands
import os
import json
import re
from urllib.parse import urlparse

BOT_TOKEN=os.environ['forumannouce-bot-API-TOKEN']
SETTING_JSON="settings.json"
SEND_CHANNEL_ID='send_messagechannel_ID'
intents = discord.Intents.default()
intents.members = True # メンバー管理の権限
intents.message_content = True # メッセージの内容を取得する権限

bot = discord.Client(intents=intents) # 権限を設定
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    print("login!")
    await tree.sync()#スラッシュコマンドを同期

@bot.event
async def on_thread_create(thread: discord.Thread):
    print("new tread!\n tread type:"+str(thread.parent.type))
    if(thread.parent.type==discord.ChannelType.forum): #forumの新規ポストを監視する
        print("new post!")
        with open(SETTING_JSON,'r')as f:#設定用json読み込み
            settings=json.load(f)
        send_channel=bot.get_channel(settings[SEND_CHANNEL_ID])
        await send_channel.send(thread.jump_url+" in "+thread.parent.jump_url)

@bot.event
async def on_message(message:discord.Message):
  if(message.type==discord.MessageType.default):
    links=re.findall('https?://[\w/:%#\$&\?\(\)~\.=\+\-]+',message.content)
    if(len(links)>0):
      for link in links:
        parse_url=urlparse(link)
        print(parse_url)
        if(parse_url.netloc=="x.com"):
          print(parse_url.scheme)
          await message.channel.send(content=str(parse_url.scheme)+"://"+"fxtwitter.com"+str(parse_url.path)+str(parse_url.query))
          
@tree.command(name="frgs",description="フォーラム通知を流すチャンネルをこのチャンネルに設定します")
async def test_command(interaction: discord.Interaction):
    
    with open(SETTING_JSON,'r')as f:#設定用json読み込み
        settings=json.load(f)
        
    settings['send_messagechannel_ID']=interaction.channel_id #コマンドが呼び出されたチャンネルIDを保存
    with open(SETTING_JSON,'w')as f:
        json.dump(settings,f)
    await interaction.response.send_message('通知チャンネル設定しました ID:'+str(interaction.channel_id),ephemeral=False)
bot.run(BOT_TOKEN)