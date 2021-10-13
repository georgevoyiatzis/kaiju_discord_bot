import os, random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

announcements_ch_id = 892056910356946954 #announcements ch_id

@client.event
async def on_message(message):
    if message.content.split(" ")[0] == "!whitelist":
        await message.channel.send(':clown:')
    elif message.content.split(' ')[0] == "!roar":
        await message.channel.send('ROAAAAAAARRRR')
    elif message.content.split(' ')[0] == "!godzilla":
        randomFile = "./assets/" + random.choice(os.listdir("./assets")) 
        with open(randomFile, 'rb') as f:
            gif = discord.File(f)
            await message.channel.send(file=gif)
    elif message.content.split(' ')[0] == "!memes":
        memesfile = "./kaiju memes/" + random.choice(os.listdir("./kaiju memes"))
        with open(memesfile, 'rb') as f:
            meme = discord.File(f)
            await message.channel.send(file=meme)
    elif message.content.split(' ')[0] == "!art":
        artfile = "./art/" + random.choice(os.listdir("./art"))
        with open(artfile, 'rb') as f:
            art = discord.File(f)
            await message.channel.send(file=art)
    elif message.content.split(' ')[0] == "!links":
        await message.channel.send("Official site: https://kaijukingz.io/#/ \nOfficial OpenSea Collection: https://opensea.io/collection/kaiju-kingz \nOfficial Contract: https://etherscan.io/address/0x1685133a98e1d4fc1fe8e25b7493d186c37b6b24")
    elif message.content.split(" ")[0] == "!opensea":
        await message.channel.send("Official OpenSea Collection: https://opensea.io/collection/kaiju-kingz")
    elif message.content.split(" ")[0] == "!wensale":
        guild = message.guild
        announcements_ch = guild.get_channel(announcements_ch_id)
        await message.channel.send(f"Please refer to {announcements_ch.mention}!")
    elif message.content.split(" ")[0] == "!ode":
        await message.channel.send('Kaiju Kings isn’t just an NFT, its a cultural reset, its the oxygen you breathe, its a lifestyle, a reason to breathe, an escape from this cruel world filled with thieves, its an art, the first gift you open on christmas, a hug from a loved one, everything you’ve ever wanted.')
    elif message.content.split(" ")[0] == "!help":
        await message.channel.send("**Kaiju Bot Commands:\n!roar\n!whitelist\n!opensea\n!wensale\n!ode\n!links\n!godzilla**")
client.run(TOKEN)
