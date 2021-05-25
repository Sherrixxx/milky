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

token = os.environ.get('BOT_TOKEN')