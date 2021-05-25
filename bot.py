import discord
from discord.ext import commands
import os

from pymongo import MongoClient
client = commands.Bot(command_prefix = 'm.')
client.remove_command('help')
cluster = MongoClient("mongodb+srv://morgenshtern:tupaparolotbotaklassno@gg-wp.tltaz.mongodb.net/morgenshtern?retryWrites=true&w=majority")
collection = cluster.ecodb.colldb


@client.event
async def on_ready():
    print('Зарегистрирован в {0}.'.format(client.user))

    for guild in client.guilds:
        for member in guild.members:
            post = {
                "_id": member.id,
                "cash": 0,
                "rep": 0,
                "lvl": 1
            }

            if collection.count_documents({"_id": member.id}) == 0:
                collection.insert_one(post)

@client.event
async def on_member_join(member):
    post = {
        "_id": member.id,
        "cash": 0,
        "rep": 0,
        "lvl": 1
    }

    if collection.count_documents({"_id": member.id}) == 0:
        collection.insert_one(post)

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle,activity=discord.Game("m.help"))

@client.command( pass_context = True )

async def help( ctx ):
	await ctx.send( 'Бот в разработке :D' )

@client.command( pass_context = True )

async def sus( ctx ):
	await ctx.send( 'SUS :flushed::flushed::flushed::flushed::flushed::flushed::flushed:AMOGUS:flushed::flushed::astonished::astonished::face_with_monocle: **42**:flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed: لماذا قمت بترجمة ذلك  :cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy:**424242424242**:flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed: https://c.tenor.com/h99LQHUExJIAAAAM/19dollar-fortnite-card-among-us.gif ')

@client.command( pass_context = True )

async def uembed( ctx ):
        await ctx.send(embed=embed)
embed=discord.Embed(title="**Проверка окда**", description="Я бот Milky (Way)", color=0x9107ed)
embed.set_thumbnail(url="https://i.pinimg.com/originals/30/88/e1/3088e1abbefe13a1754bd56deafcde2d.jpg")

@client.command( pass_context = True )

async def snus( ctx ):
        await ctx.send(embed=embed)
embed=discord.Embed(title="**Попався, снюсоед проклятый!**", url="https://youtu.be/dQw4w9WgXcQ", description="Верни снюс, иначе взломаю попу :D", color=0x9107ed)
embed.set_thumbnail(url="https://media1.tenor.com/images/c658fa9f7884021318a505266144949c/tenor.gif?itemid=15184964")
# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

import asyncio

import discord
import youtube_dl

from discord.ext import commands

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def init(self, source, *, data, volume=0.5):
        super().init(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command()
async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {query}')

    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command()
    async def stop(self, ctx):
"""Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Relatively simple music bot example')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.add_cog(Music(bot))


token = os.environ.get('BOT_TOKEN')

client.run(str(token))
