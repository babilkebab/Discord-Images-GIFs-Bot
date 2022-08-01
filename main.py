import discord

TOKEN = "MTAwMzA3NDU4NzQ3MjQ0MTM5NA.GP_3n5.njwOp4Vi6lZtGWo3OnT3Q5hRXaGiCZpw_poG5o"

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