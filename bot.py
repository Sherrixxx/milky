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

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle,activity=discord.Game(" m.help | discord.gg/r2SMG8FCQn"))

@client.command( pass_context = True )

async def help( ctx ):
	await ctx.send( 'Бот в разработке :D' )

@client.command( pass_context = True )

async def sus( ctx ):
	await ctx.send( 'SUS :flushed::flushed::flushed::flushed::flushed::flushed::flushed:AMOGUS:flushed::flushed::astonished::astonished::face_with_monocle: **42**:flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed: لماذا قمت بترجمة ذلك  :cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy:**424242424242**:flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed: https://c.tenor.com/h99LQHUExJIAAAAM/19dollar-fortnite-card-among-us.gif ')

@client.command( pass_context = True )

async def snus( ctx ):
    embed=discord.Embed(title="**Попався, снюсоед проклятый!**", url="https://youtu.be/dQw4w9WgXcQ", description="Верни снюс, иначе взломаю попу :D", color=0x9107ed)
    embed.set_thumbnail(url="https://media1.tenor.com/images/c658fa9f7884021318a505266144949c/tenor.gif?itemid=15184964")
    await ctx.send(embed=embed)

@client.command( pass_context = True )

async def credits( ctx ):
    embed=discord.Embed(description="Вы все знаете, что я не мог создаваться сам по себе :D. Да, у меня есть люди, которые вдохнули в меня жизнь! **Вау, кто же это?**  \n \n**━━━━━━━━━━━━━━━━━━━━━** \n**`Sherry#7700`** — Мой создатель. \n**`Orz#6943`** — Помогал моему создателю с моим оживлением. \n**━━━━━━━━━━━━━━━━━━━━━**  \n \nОфициальный сервер в честь меня: **===>** [Тык =)](https://discord.gg/r2SMG8FCQn)")
    embed.set_thumbnail(url="https://i.imgur.com/bk1lX1D.png")
    await ctx.send(embed=embed)

@client.command( pass_context = True )

async def ударить(ctx, member: discord.Member = None):
    gifs_punch=["https://img.gifmagazine.net/gifmagazine/images/656808/original.gif", "гифка 2"]
    ударить=random.choice(gifs_punch)
    await ctx.send(ударить)
    if member is None:
        return await ctx.send("Ты что, воздух ударил?")
    embed=discord.Embed(title="Удар", description = "{0.mention} ударил {1}.".format(ctx.author, member.mention), color=0xfff700)
    embed.set_image(url="https://img.gifmagazine.net/gifmagazine/images/656808/original.gif")
    await ctx.send(embed=embed)

token = os.environ.get('BOT_TOKEN')

client.run(str(token))
