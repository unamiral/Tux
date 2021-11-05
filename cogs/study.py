import discord, math
from discord.ext import commands
from mlconjug3 import Conjugator


class Study(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def conj(self, ctx, *, verbe):
        cg = Conjugator(language="fr")
        verb = cg.conjugate(verbe)
        res = verb.conjug_info['Indicatif']
        # 'Présent', 'Imparfait', 'Futur', 'Passé Simple'
        embed = discord.Embed(
        title=f"Conjugaison",
        description="A tool for conjugate verbs in french.",
        color=0x109319)
        embed.set_thumbnail(
        url=
        "https://media.wired.com/photos/59fccff22d3f5732c7d5aa15/master/w_2560%2Cc_limit/Pong-TA-B1C1YX.jpg")
        embed.add_field(name="Présent", value=f"Je **{res['Présent']['1s']}**,  Tu **{res['Présent']['2s']}**,  Il/Elle/On **{res['Présent']['3s']}**,  Nous **{res['Présent']['1p']}**,  Vous **{res['Présent']['2p']}**,  Ils/Elles **{res['Présent']['3p']}**", inline=False)
        embed.add_field(name="Imparfait", value=f"Je **{res['Imparfait']['1s']}**\n Tu **{res['Imparfait']['2s']}**\n Il/Elle/On **{res['Imparfait']['3s']}**\n Nous **{res['Imparfait']['1p']}**\n Vous **{res['Imparfait']['2p']}** \n Ils/Elles **{res['Imparfait']['3p']}**")
        embed.add_field(name="Futur", value=f"Je **{res['Futur']['1s']}**\n Tu **{res['Futur']['2s']}**\n Il/Elle/On **{res['Futur']['3s']}**\n Nous **{res['Futur']['1p']}**\n Vous **{res['Futur']['2p']}**\n Ils/Elles **{res['Futur']['3p']}**")
        embed.add_field(name="Passé Simple", value=f"Je **{res['Passé Simple']['1s']}**\n Tu **{res['Passé Simple']['2s']}**\n Il/Elle/On **{res['Passé Simple']['3s']}**\n Nous **{res['Passé Simple']['1p']}**\n Vous **{res['Passé Simple']['2p']}**\n Ils/Elles **{res['Passé Simple']['3p']}**")
        embed.set_footer(text="made with mlconjug3")
        embed.set_author(name="French",  icon_url="https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1200px-Flag_of_France.svg.png")
        embed.set_thumbnail(url="https://colanguage.s3.amazonaws.com/styles/find-online-teacher-profile-picture/s3/Conjugaison.png?itok=zvhKZH4D")
        await ctx.send(embed=embed)

    @commands.command()
    async def pi(self, ctx):
      await ctx.reply(math.pi)

    @commands.command()
    async def euler(self, ctx):
      await ctx.reply(math.e)

def setup(bot):
    bot.add_cog(Study(bot))
