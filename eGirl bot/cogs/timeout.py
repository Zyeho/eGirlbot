import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='=')

class ModOnlyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_mod(ctx):
        return ctx.message.author.permissions_in(ctx.channel).manage_roles

    @commands.command(name='timeout')
    @commands.check(is_mod)
    async def timeout(self, ctx, member: discord.Member, duration: int, *, reason=None):
        timeout_role = discord.utils.get(ctx.guild.roles, name='timeout')
        await member.add_roles(timeout_role, reason=reason)
        await ctx.send(f'Has sido aislado {member.mention} durante {duration} segundos')
        await asyncio.sleep(duration)
        await member.remove_roles(timeout_role, reason=reason)

bot.add_cog(ModOnlyCommands(bot))