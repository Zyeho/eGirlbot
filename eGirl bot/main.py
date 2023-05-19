import discord
import os 

from discord.ext import commands

bot = commands.Bot(command_prefix="=")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print("El bot aún no esta listo")

bot.run("MTA1MjcxMjc1NjQ0MjMxNjg5MA.GuM87D.aKgN2EMTrgv8howU4u6_e-OtuwnMhFL1TBLESU")
