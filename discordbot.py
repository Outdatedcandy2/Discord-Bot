#Discord Bot Made by Outdatedcandy92
from this import d
from typing import Text
from unicodedata import decimal
import discord
from discord.ext import commands
import time
import random
from cryptography.fernet import Fernet



TOKEN = 'MTAyODM3Njc2Mzg1Nzg5NTYzNQ.Ggh6km.qjGC0XFbP3lJaRxLbtnCnnlni5w56X9QF1A9So' #Your Discord Bot Token
CHANNEL = 1028375314742640724 #ID Of The Channel In Which You Want to Send Messages



bot = commands.Bot(command_prefix="$", intents=discord.Intents.all()) #Setting Up Bot Prefix

uppercase_letters ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits ="0123456789"
symbols="~!@#$%^&*()_+}{:?=- "


upper, lower, nums, syms =True, True ,True ,True


all=""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols    



length = 12
amount = 1
file=open('key.key','rb')
key = file.read()
file.close()
f = Fernet(key)





@bot.event #Prints That The Bot Is Online In The Terminal And In The Channel
async def on_ready():
    print("Hello! Dev Bot is Online") 
    channel = bot.get_channel(CHANNEL)
    await channel.send("Hello! Dev Bot Is Online")


@bot.command()  #Creates A Command So That When We Type $hello The Bot Replies With Hi
async def hello(ctx):
    time.sleep(1)
    await ctx.send("Hi")

@bot.command()
async def genpass(ctx):
    await ctx.message.add_reaction("👍")
    for x in range(amount):
        password ="".join(random.sample(all, length))
        embed = discord.Embed(
            title='Password Generated',
            description=password
        )

        await ctx.send(embed=embed)
        await ctx.send("DELETING IN 60 SECONDS")
        time.sleep(60)
        await ctx.channel.purge(limit=2)

@bot.command(aliases=['purge'])
async def clear(ctx, amount=30):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Successfully Deleted The Messages")


@bot.command()
async def encrypt(ctx):
    f = Fernet(key)
    await ctx.send("Send Message To Encrypt")
    message = await bot.wait_for('message')
    msg = bytes(message.content, 'utf-8')

    print(message.content)

    pw = f.encrypt(msg)
    print(pw)
    embed=discord.Embed(
        title='Encrypted Text',
        description=str(pw,'utf8')
    )
    await ctx.author.send(embed=embed)

@bot.command()
async def decrypt(ctx):
    f2 = Fernet(key)
    await ctx.send("Send Message To Decrypt")
    message = await bot.wait_for('message')
    msg = bytes(message.content,'utf-8')
    print(msg)
    pw = f2.decrypt(msg)
    print(pw)
    embed=discord.Embed(
    title='Decrypted Text',
    description=str(pw,'utf8')
    )
    await ctx.author.send(embed=embed)

@bot.command()
async def message(ctx, user:discord.Member, *, message=None):
    message = "Test Dm"
    embed=discord.Embed(title=message)
    await user.send(embed=embed)



    



bot.run(TOKEN) #Run The Bot