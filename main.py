import discord
import os

from ping import keep_alive
from discord.ext import commands




bot = commands.Bot(command_prefix="?", help_command=Help())


@bot.event
async def on_ready():
    print(f"\a Bot has logged in as {bot.user}")
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name="?help"))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        embed = discord.Embed(title=":x: Command Not Founded", color=0xc40906)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(
            title=":x: Please Pass In All Of The Missing Required Argument",
            color=0xc40906)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.errors.MissingPermissions):
        embed = discord.Embed(
            title=":x: Sorry! But You Don't Have Enough Permissions To Run This Command",
            color=0xc40906)
        await ctx.send(embed=embed)

    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title=":x: Please Pass In All Of The Required Argument Correctly",
            color=0xc40906)
        await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title=f"Pong! {round(bot.latency * 1000)}ms",
        description="This is a tool for measure latency of bot.",
        color=0x109319)
    embed.set_thumbnail(
        url="https://media.wired.com/photos/59fccff22d3f5732c7d5aa15/master/w_2560%2Cc_limit/Pong-TA-B1C1YX.jpg"
    )
    await ctx.send(embed=embed)


def is_me(ctx):
    return ctx.author.id == 829306875076935680


@bot.command()
@commands.check(is_me)
async def load(ctx, ext):
    bot.load_extension(f"cogs.{ext}")
    embed = discord.Embed(title=f"{ext} has loaded.",
                          description="For load cogs",
                          color=0x109319)
    embed.set_thumbnail(
        url="https://static1.smartbear.co/smartbear/media/blog/wp/heavy-load.jpg")
    await ctx.send(embed=embed)


@bot.command()
@commands.check(is_me)
async def unload(ctx, ext):
    bot.unload_extension(f"cogs.{ext}")
    embed = discord.Embed(title=f"{ext} has unloaded.",
                          description="For unload cogs",
                          color=0xc40906)
    embed.set_thumbnail(url="https://i.imgur.com/05De7kW.png")
    await ctx.send(embed=embed)


@bot.command()
@commands.check(is_me)
async def reload(ctx, ext):
    bot.unload_extension(f"cogs.{ext}")
    bot.load_extension(f"cogs.{ext}")
    embed = discord.Embed(title=f"{ext} has reloaded.",
                          description="For reload cogs",
                          color=0x109319)
    embed.set_thumbnail(
        url="https://cdn2.iconfinder.com/data/icons/ios-7-icons/50/reload-512.png")
    await ctx.send(embed=embed)


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


keep_alive()
bot.run(os.getenv("TOKEN"))
