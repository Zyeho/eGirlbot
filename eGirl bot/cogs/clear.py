import discord
from discord.ext import commands

class ClearCog(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.command(name="clear", description="Borrar mensajes!")
  async def clear(self, ctx: commands.Context, num_messages: int):
    if ctx.author.guild_permissions.manage_messages:
      if num_messages > 300:
        await ctx.send("Lo siento, no puedes borrar más de 300 mensajes a la vez.")
      else:
        await ctx.channel.purge(limit=num_messages)
        await ctx.send(f"{num_messages} mensajes eliminados correctamente.")
    else:
      await ctx.send("Lo siento, no tienes permiso para borrar mensajes.")

async def setup(client:commands.Bot) -> None:
  await client.add_cog(ClearCog(client))




