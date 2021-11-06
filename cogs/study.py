import discord
import math
from discord.ext import commands
from mlconjug3 import Conjugator


class Study(commands.Cog):
    """This is a module for help you in study!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def conj(self, ctx, *, verbe):
        """For Conjugate verb in french. Usage: `?conj VERBE`"""
        cg = Conjugator(language="fr")
        verb = cg.conjugate(verbe)
        res = verb.conjug_info['Indicatif']
        embed = discord.Embed(
            title=f"Conjugaison",
            description="A tool for conjugate verbs in french.",
            color=0x109319)
        embed.set_thumbnail(
            url="https://media.wired.com/photos/59fccff22d3f5732c7d5aa15/master/w_2560%2Cc_limit/Pong-TA-B1C1YX.jpg")
        embed.add_field(
            name="Présent",
            value=f"Je **{res['Présent']['1s']}**\n  Tu **{res['Présent']['2s']}**\n  Il/Elle/On **{res['Présent']['3s']}**\n  Nous **{res['Présent']['1p']}**\n  Vous **{res['Présent']['2p']}**\n  Ils/Elles **{res['Présent']['3p']}**\n")
        embed.add_field(
            name="Imparfait",
            value=f"Je **{res['Imparfait']['1s']}**\n Tu **{res['Imparfait']['2s']}**\n Il/Elle/On **{res['Imparfait']['3s']}**\n Nous **{res['Imparfait']['1p']}**\n Vous **{res['Imparfait']['2p']}** \n Ils/Elles **{res['Imparfait']['3p']}**")
        embed.add_field(
            name="Futur",
            value=f"Je **{res['Futur']['1s']}**\n Tu **{res['Futur']['2s']}**\n Il/Elle/On **{res['Futur']['3s']}**\n Nous **{res['Futur']['1p']}**\n Vous **{res['Futur']['2p']}**\n Ils/Elles **{res['Futur']['3p']}**")
        embed.add_field(
            name="Passé Simple",
            value=f"Je **{res['Passé Simple']['1s']}**\n Tu **{res['Passé Simple']['2s']}**\n Il/Elle/On **{res['Passé Simple']['3s']}**\n Nous **{res['Passé Simple']['1p']}**\n Vous **{res['Passé Simple']['2p']}**\n Ils/Elles **{res['Passé Simple']['3p']}**")
        embed.set_footer(text="made with mlconjug3")
        embed.set_author(
            name="French",
            icon_url="https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1200px-Flag_of_France.svg.png")
        embed.set_thumbnail(
            url="https://colanguage.s3.amazonaws.com/styles/find-online-teacher-profile-picture/s3/Conjugaison.png?itok=zvhKZH4D")
        await ctx.send(embed=embed)

    @commands.command()
    async def pi(self, ctx):
        """For send our old famous irrational number, PI. Usage : `?pi`"""
        embed = discord.Embed(title=f"Pi is {math.pi}", color=0x109319)
        embed.set_footer(
            text="The number π (/paɪ/; spelled out as \"pi\") is a mathematical constant, approximately equal to 3.14159. It is defined in Euclidean geometry[a] as the ratio of a circle's circumference to its diameter, and also has various equivalent definitions. The number appears in many formulas in all areas of mathematics and physics. The earliest known use of the Greek letter π to represent the ratio of a circle's circumference to its diameter was by Welsh mathematician William Jones in 1706.[1]It is also referred to as Archimedes's constant. wikipedia")
        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Pi-symbol.svg/1058px-Pi-symbol.svg.png")
        embed.set_author(name="Math", icon_url="https://upload.wikimedia.org/wikipedia/commons/7/7b/Math.png")
        await ctx.send(embed=embed)

    @commands.command(aliases=["e"])
    async def euler(self, ctx):
        """For send our old cozy irrational number, e(euler's number). Usage : `?euler` or `?e`"""
        embed = discord.Embed(title=f"e is {math.e}", color=0x109319)
        embed.set_footer(text="The number e, also known as Euler's number, is a mathematical constant approximately equal to 2.71828, and can be characterized in many ways. It is the base of the natural logarithm. It is the limit of ⁿ as n approaches infinity, an expression that arises in the study of compound interest. wikipedia")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/cb/d9/cf/cbd9cf526ee707aafc7a51488c7c2c49.png")
        embed.set_author(name="Math", icon_url="https://upload.wikimedia.org/wikipedia/commons/7/7b/Math.png")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Study(bot))
