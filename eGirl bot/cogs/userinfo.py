import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):

        name = f"{member.name}#{member.discriminator}"
        
        user_id = member.id
        
        status = member.status
        
        created_at = member.created_at
        
        highest_role = member.top_role
        
        join_date = member.joined_at
        
        avatar_url = member.avatar_url
        
        embed = discord.Embed(title=name, description=f"ID: {user_id}")
        embed.add_field(name="Status", value=status)
        embed.add_field(name="Account created at", value=created_at)
        embed.add_field(name="Highest role", value=highest_role)
        embed.add_field(name="Joined server at", value=join_date)
        embed.set_thumbnail(url=avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UserInfo(bot))
