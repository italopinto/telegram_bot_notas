import logging
from os import getenv
from dotenv import load_dotenv
from telegrampy.ext.commands.errors import MissingRequiredArgument
from model_utils import *

import telegrampy
from telegrampy import Message
from telegrampy.ext import commands


# Configuring logging
logging.basicConfig(level=logging.INFO, format="(%(asctime)s) %(levelname)s %(message)s", datefmt="%m/%d/%y - %H:%M:%S %Z")
logger = logging.getLogger("telegrampy")


# Loading the .env variables
load_dotenv()
TOKEN = getenv('API_TOKEN')


# Initializing the bot
bot = commands.Bot(TOKEN)


@bot.event
async def on_message(message): #message é do tipo `Message`
    if message.content in ['/start', '/show', '/del_all'] or message.content[:8] in '/del_one':
        return
    else:
        data = message.content + '\n'
        if insert_table(data.lower()) == True:
            await Message.reply(message, content=f'@{message.author} nota salva com sucesso!')
        else:
            await Message.reply(message, content=f'@{message.author} ERRO! nota # {message.content} # não salva.')


"""
Bot's Functionalities
"""

# use regex to send the messages with the first letter in upper case
@bot.command()
async def show(ctx): #ctx é do tipo `context`
    if len(show_table()) == 0:
        await ctx.reply(content=f'@{ctx.author} não há notas salvas!')  
    else:
        tmp = []
        for a in show_table():
            tmp.extend([a[0]])
        await ctx.send(''.join(tmp))
        tmp.clear()


@bot.command()
async def del_all(ctx):
    if len(show_table()) == 0:
        await ctx.reply(content=f'@{ctx.author} não há notas salvas para serem apagados!')  
    else:
        delete_data()
        await ctx.send(f'Todos as notas foram apagados com sucesso @{ctx.author}!')


@bot.command()
async def del_one(ctx, arg:str):
    try:
        if arg != None:
            count = show_table()
            reminder = arg.lower()
            for i in count:
                if reminder in i[0]:
                    msg = i[0]
                    # outputs with the first letter in upper case
                    if delete_row(msg) == True:
                        await ctx.reply(content=f'@{ctx.author} nota {msg} apagada com sucesso!')
                    else:
                        await ctx.reply(content=f'@{ctx.author} ERRO! Nota {msg} não apagada!')
        elif len(show_table()) == 0:
            await ctx.reply(content=f'@{ctx.author} não há notas salvas para serem apagadas!')  
    except MissingRequiredArgument as e:
        print(e)


bot.run()
