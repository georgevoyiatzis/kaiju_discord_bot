import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.split(" ")[0] == "!whitelist":
        await message.channel.send(':clown:')

client.run(TOKEN)
