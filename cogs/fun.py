import discord, requests, random, json
from discord.ext import commands

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def get_quote(self, ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    await ctx.reply("> " + json_data[0]["q"] + "\n" + "**" + json_data[0]["a"] + "**")
  @commands.command(aliases=["8ball"])
  async def _8ball(self, ctx, *, question):
    choices = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    await ctx.reply(f"Question : {question}\n> Wise 8ball : {random.choice(choices)}")
  


def setup(bot):
  bot.add_cog(Fun(bot))
