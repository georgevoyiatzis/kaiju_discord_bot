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
    elif message.content.split(' ')[0] == "!roar":
        await message.channel.send('ROAAAAAAARRRR')
    elif message.content.split(' ')[0] == "!links":
        await message.channel.send("Official site: https://kaijukingz.io/#/ \nOfficial OpenSea Collection: https://opensea.io/collection/kaiju-kingz \nOfficial Contract: https://etherscan.io/address/0x1685133a98e1d4fc1fe8e25b7493d186c37b6b24")

client.run(TOKEN)
