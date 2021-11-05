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
        await ctx.reply(
            f"**Présent** => Je **{res['Présent']['1s']}** , Tu **{res['Présent']['2s']}** , Il/Elle/On **{res['Présent']['3s']}** , Nous **{res['Présent']['1p']}** , Vous **{res['Présent']['2p']}** , Ils/Elles **{res['Présent']['3p']}**\n**Imparfait** => Je **{res['Imparfait']['1s']}** , Tu **{res['Imparfait']['2s']}** , Il/Elle/On **{res['Imparfait']['3s']}** , Nous **{res['Imparfait']['1p']}** , Vous **{res['Imparfait']['2p']}** , Ils/Elles **{res['Imparfait']['3p']}**\n**Futur** => Je **{res['Futur']['1s']}** , Tu **{res['Futur']['2s']}** , Il/Elle/On **{res['Futur']['3s']}** , Nous **{res['Futur']['1p']}** , Vous **{res['Futur']['2p']}** , Ils/Elles **{res['Futur']['3p']}**\n**Passé Simple** => Je **{res['Passé Simple']['1s']}** , Tu **{res['Passé Simple']['2s']}** , Il/Elle/On **{res['Passé Simple']['3s']}** , Nous **{res['Passé Simple']['1p']}** , Vous **{res['Passé Simple']['2p']}** , Ils/Elles **{res['Passé Simple']['3p']}**\n> made with mlconjug3"
        )
    @commands.command()
    async def pi(self, ctx):
      await ctx.reply(math.pi)

    @commands.command()
    async def euler(self, ctx):
      await ctx.reply(math.e)

def setup(bot):
    bot.add_cog(Study(bot))
