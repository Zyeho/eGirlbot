import discord
from discord.ext import commands
import time


bot = commands.Bot(command_prefix='=')

class PingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):

        before = time.perf_counter()
        message = await ctx.send('Pinging...')

        after = time.perf_counter()
        ping = (after - before) * 1000

        embed = discord.Embed(title='Ping', color=discord.Color.purple())
        embed.add_field(name='Pong! La latencia es de', value=f'{ping:,.2f} ms')
        await message.edit(embed=embed)


bot.add_cog(PingCommands(bot))