import discord

TOKEN = "MTAwMzA3NDU4NzQ3MjQ0MTM5NA.GlAVQI.OZ5oO1RSv3ZVtUlxIc2Bq1SaUCz2czP7MmGLQo"

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
