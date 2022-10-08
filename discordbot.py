#Discord Bot Made by Outdatedcandy92
import discord
from discord.ext import commands

TOKEN = 'MTAyODM3Njc2Mzg1Nzg5NTYzNQ.GMhOf6.GId8x8WSKbaxFo92Qr0aUHjlZjefYi6Kiyy9WU' #Your Discord Bot Token
CHANNEL = 1028375314742640724 #ID Of The Channel In Which You Want to Send Messages

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all()) #Setting Up Bot Prefix



@bot.event #Prints That The Bot Is Online In The Terminal And In The Channel
async def on_ready():
    print("Hello! Dev Bot is Online") 
    channel = bot.get_channel(CHANNEL)
    await channel.send("Hello! Dev Bot Is Online")


@bot.command()  #Creates A Command So That When We Type $hello The Bot Replies With Hi
async def hello(ctx):
    await ctx.send("Hi")



bot.run(TOKEN) #Run The Bot