import discord
import typing
import wavelink

from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.create_nodes())
    
    async def create_nodes(self):
        await self.bot.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.bot, host="127.0.0.1", port="2333", password="youshallnotpass", region="asia")
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is now ready!")

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f"Node <{node.identifier}> is now Ready!")
    
    @commands.command(name="join", aliases=["connect", "summon"])
    async def join_command(self, ctx: commands.Context, channel: typing.Optional[discord.VoiceChannel]):
        if channel is None:
            channel = ctx.author.voice.channel
        
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if player is not None:
            if player.is_connected():
                return await ctx.send("El bot está conectado en el canal de voz.")
        
        await channel.connect(cls=wavelink.Player)
        mbed=discord.Embed(title=f"Se ha conectado a {channel.name}", color=discord.Color.purple)
        await ctx.send(embed=mbed)

    @commands.command(name="leave", alises=["disconnect"])
    async def leave_command(self, ctx: commands.Context):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if player is None:
            return await ctx.send("El bot no está conectado a ningún canal de voz.")
        
        await player.disconnect()
        mbed = discord.Embed(title="Disconnected", color=discord.Color.purple)
        await ctx.send(embed=mbed)
    
    @commands.command(name="play")
    async def play_command(self, ctx: commands.Context, *, search: str):
        search = await wavelink.YouTubeTrack.search(query=search, return_first=True)

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client
        
        await vc.play(search)

        mbed = discord.Embed(title=f"Reproduciendo ahora: {search}", color=discord.Color.purple)
        await ctx.send(embed=mbed)
    
    @commands.command(name="stop")
    async def stop_command(self, ctx: commands.Context):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if player is None:
            return await ctx.send("El bot no está conectado a ningún canal de voz.")
        
        if player.is_playing:
            await player.stop()
            mbed = discord.Embed(title="Playback Stoped", color=discord.Color.purple)
            return await ctx.send(embed=mbed)
        else:
            return await ctx.send("Nada se está reproduciendo ahorita mismo.")
    
    @commands.command(name="pause")
    async def pause_command(self, ctx: commands.Context):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if player is None:
            return await ctx.send("El bot no está conectado a ningún canal de voz")
        
        if not player.is_paused():
            if player.is_playing():
                await player.pause()
                mbed = discord.Embed(title="Playback Paused", color=discord.Color.purple)
                return await ctx.send(embed=mbed)
            else:
                return await ctx.send("Nada se esta reproduciendo ahorita mismo")
        else:
            return await ctx.send("Playback is Already paused")
    
    @commands.command(name="resume")
    async def resume_command(self, ctx: commands.Context):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if player is None:
            return await ctx.send("El bot no está conectado a ningún canal de voz")
        
        if player.is_paused():
            await player.resume()
            mbed = discord.Embed(title="Playback resumed", color=discord.Color.purple)
            return await ctx.send(embed=mbed)
        else:
            return await ctx.send("playback is not paused")

    @commands.command(name="volume")
    async def volume_command(self, ctx: commands.Context, to: int):
        if to > 100:
            return await ctx.send("El volumen debe estar entre 0 y 100")
        elif to < 1:
            return await ctx.send("El volumen debe estar entre 0 y 100")
        

        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        await player.set_volume(to)
        mbed = discord.Embed(title=f"Volumen cambiado a {to}", color=discord.Color.purple)
        await ctx.send(embed=mbed)

def setup(client):
    client.add_cog(Music(client))