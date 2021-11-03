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


@bot.command(aliases=["8ball"])
async def eightball(ctx, *, qn):
    await ctx.send(f"Question : {qn}\nAnswer : {backend._8ball()}")


@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked : {member.mention}")


@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned : {member.mention}")

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
  bans = await ctx.guild.bans()
  member_name, member_discriminator = member.split("#")
  for ban_entry in bans:
    user = ban_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f"Unbanned : {user.mention}")
      return
keep_alive()
bot.run(os.getenv("TOKEN"))
