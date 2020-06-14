import discord
from discord.ext import commands

import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='[')
ch = bot.get_channel(id)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(721588040530919504) 
    print(f"{member} join!")
    await channel.send(f"{member} 歡迎加入:kissing_closed_eyes:!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(721588040530919504)
    print(f"{member} leave!")
    await channel.send(f"{member} 離開了.....:tired_face:") 

@bot.event
async def on_message(msg):
    if msg.content == '堀北鈴音':
     await msg.channel.send('hi')


@bot.command()
async def 幹你娘(ctx):
    await ctx.send('幹你娘')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def 堀北鈴音1(ctx):
    pic= discord.File(jdata['pic1'])
    await ctx.send(file=pic)

@bot.command()
async def 堀北鈴音2(ctx):
    pic= discord.File(jdata['pic2'])
    await ctx.send(file=pic)

@bot.command()
async def 堀北鈴音3(ctx):
    pic= discord.File(jdata['pic3'])
    await ctx.send(file=pic)

@bot.command()
async def 堀北鈴音4(ctx):
    pic= discord.File(jdata['pic4'])
    await ctx.send(file=pic)

bot.run('NzIxNTUyOTYzODk3OTE3NDQ0.XuWMpA.eW9DiTFTyAgF4cqYnSnm--muOD4')