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

@client.command(pass_context=True, brief="Бот присоединится к голосовому каналу.", aliases=['j', 'jo'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("<:milky_cross:846709234204934174> Вы не в голосовом канале!")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"<:milky_tick:846709199747809281> Уже захожу в **{channel}**!")

@client.command(pass_context=True, brief="This will play a song 'play [url]'", aliases=['pl'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music end or use the 'stop' command")
        return
    await ctx.send("Getting everything ready, playing audio soon")
    print("Someone wants to play music let me get that ready for them...")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()


token = os.environ.get('BOT_TOKEN')

client.run(str(token))
