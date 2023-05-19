import discord
import spotipy
from discord.ext import commands
from spotipy.oauth2 import SpotifyClientCredentials

bot = commands.Bot(command_prefix='=')

class SpotifyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def play(self, ctx, *, query):

        client_credentials_manager = SpotifyClientCredentials(client_id="f847eade91634c259f58b00c8dfecc94", client_secret="cda56efb566e45a0afd58568688dbab3")
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        results = sp.search(q=query, type='track,playlist')

        if results['tracks']['total'] == 0 and results['playlists']['total'] == 0:
            return await ctx.send('No results found')


        result = results['tracks']['items'][0] if results['tracks']['total'] > 0 else results['playlists']['items'][0]

        if result['type'] == 'track':

            await ctx.send(f'Reproducing song: {result["name"]}')
        else:

            await ctx.send(f'Reproducing playlist: {result["name"]}')

bot.add_cog(SpotifyCommands(bot))





