import discord
from discord.ext import commands
import os
import random
from discord import utils
from discord.utils import get

from pymongo import MongoClient
client = commands.Bot(command_prefix = 'm.')
client.remove_command('help')
cluster = MongoClient("mongodb+srv://morgenshtern:tupaparolotbotaklassno@gg-wp.tltaz.mongodb.net/morgenshtern?retryWrites=true&w=majority")
collection = cluster.ecodb.colldb

borodar = [ 'Да', 'да', 'дА', 'дa', 'дA' ]
boroda = [ 'Da', 'da', 'dA', 'dа', 'dА' ]

@client.command()
async def say(ctx,* arg):
    await ctx.send(" ".join(arg))

@client.event
async def on_ready():
    print('Зарегистрирован в {0}.'.format(client.user))

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online,activity=discord.Game(" m.help"))

@client.command( pass_context = True )
async def help( ctx ):
	await ctx.send( 'Бот в разработке :D' )

@client.command(pass_context= True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send( '<:milky_cross:846709234204934174> Я не понял, кого мне кинуть?' )
        return
    await member.kick()
    await ctx.send( '<:milky_tick:846709199747809281> **{0}#{1}** Был изгнан из этого места!'.format(member.name, member.discriminator))

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
      await ctx.send( '<:milky_cross:846709234204934174> Что-то мне кажется, что у тебя силёнок нет для этой команды.' )

@client.command(pass_context= True)
@commands.has_permissions(manage_roles=True)
async def мут(ctx, member: discord.Member=None):
    if not member:
        await ctx.send( '<:milky_cross:846709234204934174> И зачем я закрыл рот воздуху?' )
        return
    await ctx.send( '<:milky_tick:846709199747809281> Я заклеил **{0}#{1}** рот!'.format(member.name, member.discriminator))
    role = discord.utils.get(ctx.guild.roles, name="В муте")
    await member.add_roles(role)

@мут.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send( '<:milky_cross:846709234204934174> У тебя нет скотча.' )

@client.command()
async def пинг(ctx):
    ping = round(Bot.latency * 1000)
    await ctx.send(f" Мой пинг: `**{ping} MS**`")

@client.command( pass_context = True )
async def sus( ctx ):
	await ctx.send( 'SUS :flushed::flushed::flushed::flushed::flushed::flushed::flushed:AMOGUS:flushed::flushed::astonished::astonished::face_with_monocle: **42**:flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed: لماذا قمت بترجمة ذلك  :cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy::cowboy:**424242424242**:flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed::flushed: https://c.tenor.com/h99LQHUExJIAAAAM/19dollar-fortnite-card-among-us.gif ')

@client.command(name='шар', pass_context= True)
async def шар(ctx, arg):
        if arg != '':
            messages = [':thumbsup: Да.', ':thumbsdown: Нет.', ':green_book: Эта книжка говорит... **Да!**', ':closed_book: Эта книжка говорит... **Нет!**', ':compass: Стрелка показывает на... **Да!**', ':pensive: Я устал, **не трогай меня...**', 'Да **неееет.**', 'Однозначно **да!**', '**Конечно!**', 'Ты ещё спрашиваешь? П-фф, **конечно да!**', 'Эм, **точно нет.**', ':person_bouncing_ball: Я побежал есть пельмени, не хочу отвечать.']
            kv1 = int(len(messages))
            messages_output = messages.pop(random.randint(0, kv1 - 1))
            await ctx.send(f'{messages_output}')

@client.command( pass_context = True )
async def on_message( message ):
    msg = message.content.lower()

    if msg in borodar:
        await message.channel.send( '🧔 **Борода**' )

    if msg in borodar:
        await message.channel.send( '🧔 **Борода**' )

    if msg in boroda:
        await message.channel.send( '🧔 **Boroda**' )

    if msg in boroda:
        await message.channel.send( '🧔 **Boroda**' )

@client.command( pass_context = True )
async def snus( ctx ):
    embed=discord.Embed(title="**Попався, снюсоед проклятый!**", url="https://youtu.be/dQw4w9WgXcQ", description="Верни снюс, иначе взломаю попу :D", color=0x9107ed)
    embed.set_thumbnail(url="https://media1.tenor.com/images/c658fa9f7884021318a505266144949c/tenor.gif?itemid=15184964")
    await ctx.send(embed=embed)

@client.command( pass_context = True )
async def credits( ctx ):
    embed=discord.Embed(description="Вы все знаете, что я не мог создаваться сам по себе :D. Да, у меня есть люди, которые вдохнули в меня жизнь! **Вау, кто же это?**  \n \n**━━━━━━━━━━━━━━━━━━━━━** \n**`Sherry#7700`** — Мой создатель. \n**`Orz#6943`** — Помогал моему создателю с моим оживлением. \n**━━━━━━━━━━━━━━━━━━━━━**  \n \nОфициальный сервер в честь меня: \n**===>** [Тык =)](https://discord.gg/r2SMG8FCQn)")
    embed.set_thumbnail(url="https://i.imgur.com/bk1lX1D.png")
    await ctx.send(embed=embed)

@client.command( pass_context = True )
async def ударить(ctx, member: discord.Member = None):
    if member is None:
        return await ctx.send("Ты что, воздух ударил?")
    gifs_punch=['https://img.gifmagazine.net/gifmagazine/images/656808/original.gif', 'https://s3.amazonaws.com/s3.timetoast.com/public/uploads/photos/3377879/SwordFight.gif?1358704239']
    ударить=random.choice(gifs_punch)
    embed=discord.Embed(title="Удар", description = "{0.mention} ударил {1}.".format(ctx.author, member.mention), color=0xfff700)
    embed.set_image(url = gifs_punch)
    await ctx.send(embed=embed)

token = os.environ.get('BOT_TOKEN')

client.run(str(token))
