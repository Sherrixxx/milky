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

@client.command( pass_context = True )

async def credits( ctx ):
        await ctx.send(embed=embed)
embed=discord.Embed(title="**Попався, снюсоед проклятый!**", url="https://youtu.be/dQw4w9WgXcQ", description="Верни снюс, иначе взломаю попу :D", color=0x9107ed)
embed.set_thumbnail(url="https://media1.tenor.com/images/c658fa9f7884021318a505266144949c/tenor.gif?itemid=15184964")


server, server_id, name_channel = None, None, None

domains = ['https://www.youtube.com/', 'http://www.youtube.com/', 'https://youtu.be/', 'http://youtu.be/']
async def check_domains(link):
    for x in domains:
        if link.startswith(x):
            return True
    return False

@client.command()

async def play(ctx, *, command = None):
    """Включить музыку."""
    global server, server_id, name_channel
    author = ctx.author
    if command == None:
        server = ctx.guild
        name_channel = author.voice.channel.name
        voice_channel = discord.utils.get(server.voice.channels, name=name_channel)
    params = command.split(' ')
    if len(params) == 1:
        sourse = params[0]
        server = ctx.guild
        name_channel = author.voice.channel.name
        voice_channel = discord.utils.get(server.voice.channels, name=name_channel)
        print('param 1')
    elif len(params) == 3:
        server_id = params[0]
        voice_id = params[1]
        sourse = params[2]
        try:
            server_id = int(server_id)
            voice_id = int(voice_id)
        except:
            await ctx.channel.send('<:milky_cross:846709234204934174> {author.mention}, ID сервера или войса должно быть численным **:(**')
            return
        print('param 3')
        server = bot.get_guild(server_id)
        voice_channel = discord.utils.get(server.voice.channels, id=voice_id)
    else:
        await ctx.channel.send(f'<:milky_cross:846709234204934174> {author.mention} Ты неправильно написал команду **:(**')
        return

    voice = discord.utils.get(bot.voice_clients, guild = server)
    if voice is None:
        await voice_channel.connect()
        voice = discord.utils.get(bot.voice_clients, guild = server)

    if sourse == None:
        pass
    elif sourse.startswith('http'):
        if not check_domains(sourse):
            await ctx.channel.send(f'<:milky_cross:846709234204934174> {author.mention} Что это за ссылка? Кидай ссылку ютуба!')
            return
        sond_there = os.path.isfile('music/sond.mp3')
        try:
            if sond_there:
                os.remove('sond.mp3')
        except PermissionError:
            await ctx.channel.send('Недостаточно прав для удаления.')
            return
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
		}
            ],
	}

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([sourse])
        for file in os.listdir('music/'):
            if file.endswith('.mp3'):
                os.rename(file, 'sond.mp3')
        voice.play(discord.FFmpegPCMAudio('sond.mp3'))
    else:
        voice.play(discord.FFmpegPCMAudio('music/{sourse}'))

token = os.environ.get('BOT_TOKEN')

client.run(str(token))
