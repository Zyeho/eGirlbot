import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='=')

class ModOnlyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_mod(ctx):
        return ctx.message.author.permissions_in(ctx.channel).ban_members

    @commands.command(name='unban')
    @commands.check(is_mod)
    async def unban(self, ctx, user_id: int, *, reason=None):
        banned_users = await ctx.guild.bans()
        user = discord.utils.find(lambda u: u.user.id == user_id, banned_users)

        if user is None:
            return await ctx.send(f'User with ID {user_id} is not banned')

        await ctx.guild.unban(user.user, reason=reason)
        await ctx.send(f'Ha sido desbaneado {user.user.mention}')

bot.add_cog(ModOnlyCommands(bot))