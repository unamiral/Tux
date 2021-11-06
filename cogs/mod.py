import discord, asyncio
from discord.ext import commands


class DurationConverter(commands.Converter):
    async def convert(self, ctx, value):
        amount = value[:-1]
        unit = value[-1]

        if amount.isdigit() and unit in ["s", "m", "h", "d"]:
            return (int(amount), unit)
        raise commands.BadArgument()


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount=10):
        embed = discord.Embed(title=f"Delete {amount} messages in 5s")
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(ctx, member: commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title=f"Kicked : {member.mention} Because of {reason}", color=0xc40906)
        embed.set_image(url="https://c.tenor.com/CqSWwijaSIwAAAAM/ban-banned.gif")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(ctx, member: commands.MemberConverter, duration : DurationConverter ="1h" , *, reason=None):
        multiplier = {"s" : 1, "m" : 60, "h" : 3600, "d" : 86400}
        amount, unit = duration
        await member.ban(reason=reason)
        embed = discord.Embed(title=f"Banned : {member.mention} For {duration} Because of {reason}", color=0xc40906)
        embed.set_image(url="https://c.tenor.com/CqSWwijaSIwAAAAM/ban-banned.gif")
        await ctx.send(embed=embed)
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)
        embed = discord.Embed(title=f"{member.mention} Unbanned", color=0x2b75a6)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(ctx, *, member):
        bans = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in bans:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title=f"{user.mention} Unbanned", color=0x2b75a6)
                await ctx.send(embed=embed)
                return
