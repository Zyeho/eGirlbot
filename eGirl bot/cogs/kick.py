import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='=')

class ModOnlyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_mod(ctx):
        return ctx.message.author.permissions_in(ctx.channel).manage_messages

    @commands.command(name='kick')
    @commands.check(is_mod)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Has sido pateado del servidor. {member.mention}')

bot.add_cog(ModOnlyCommands(bot))