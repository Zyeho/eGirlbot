import discord
import os
from discord.ext import commands
from colorama import Back, Fore, Style
from dotenv import load_dotenv
import time
import json
import platform

load_dotenv()

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('='), intents=discord.Intents().all())

        self.cogslist = ["cogs.clear"]

    async def setup_hook(self):
      for ext in self.cogslist:
        await self.load_extension(ext)

    async def on_ready(self):
        prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python Version " + Fore.YELLOW + str(platform.python_version()))

TOKEN = os.getenv("DISCORD_API_TOKEN")
client = Client()
client.run(TOKEN)
















