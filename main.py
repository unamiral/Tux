import discord, os, random, backend

from ping import keep_alive
from replit import db
from discord.ext import commands

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print(f"\a Bot have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="?h"))

@bot.command()
async def h(ctx):
  f = open("help.txt")
  await ctx.send(f.read())
  f.close()

@bot.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

keep_alive()
bot.run(os.getenv("TOKEN"))
