import discord
from credential.py import *

<<<<<<< HEAD
TOKEN = token
=======
TOKEN = "YOUR TOKEN"
>>>>>>> a6b10c67851a11bd0a5600565a2a557875ef42a9

client = discord.Client()

@client.event

async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello there!')

client.run(TOKEN)
