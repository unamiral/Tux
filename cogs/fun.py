import discord
import requests
import random
import json
from discord.ext import commands


class Fun(commands.Cog):
    """This is module for make you laugh!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        """For send a quote from wise people. Usage: `?quote`"""
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        embed = discord.Embed(color=0x2b75a6)
        embed.set_author(
            name=json_data[0]["a"],
            icon_url="https://media.istockphoto.com/photos/magic-book-open-picture-id1210557301?b=1&k=20&m=1210557301&s=170667a&w=0&h=wWIp4fUJTG_5afInjVGrXN34ny0MSnC9xY9WAEqhl38="
        )
        embed.set_footer(text="made with api of zenquotes.io")
        embed.add_field(name="Quote Of Day", value=json_data[0]["q"])
        await ctx.send(embed=embed)

    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question):
        """For get answer for your question from wise 8ball Usage: `?8ball`"""
        choices = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.",
            "Better not tell you now.", "Cannot predict now.",
            "Concentrate and ask again.", "Don't count on it.",
            "My reply is no.", "My sources say no.", "Outlook not so good.",
            "Very doubtful."
        ]
        embed = discord.Embed(title=f"Question : {question}", color=0x2b75a6)
        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/8-Ball_Pool.svg/1024px-8-Ball_Pool.svg.png")
        embed.add_field(name="Wise 8ball Answer:", value=random.choice(choices))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
