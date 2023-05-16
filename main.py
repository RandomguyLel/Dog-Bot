from keep_alive import keep_alive
import os
import discord
from datetime import datetime
import re
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('DISCORD_PREFIX')
client = discord.Client()

client = Bot(command_prefix=list(PREFIX))

x = datetime.now()  #console time log
x = str(x)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(
        name='Woof woof Im a dog'))

    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print('Bot started at ' + x)
    print(f'{client.user} has connected to Discord!:\n'
          f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})\n'
          f'Sometimes Life is Pain\n'
          f'for da love of god stop breakin shid\n'
          f'Riperino piperino instagramerino prejecterino')


@client.event
async def on_message(message):
    if message.author == client.user:
        print('Dog is doing stuff ' + x)
        return
# Use regex to match a link starting with "https://www.instagram.com/"
    match = re.match(r'(https:\/\/www\.instagram\.com\/\S+)', message.content)

    if match:
        # Get the matched link
        link = match.group(1)
        author = message.author.name
        # Modify the link to replace "instagram" with "ddinstagram"
        modified_link = link.replace("instagram", "ddinstagram")

        # Send the modified link as a message
        await message.delete()
        await message.channel.send(f"Posted by {author}: {modified_link}")

# Use regex to match a link starting with "https://twitter.com/"
    match = re.match(r'(https:\/\/twitter\.com\/\S+)', message.content)

    if match:
        # Get the matched link
        link = match.group(1)
        author = message.author.name
        # Modify the link to replace "twitter" with "fxtwitter"
        modified_link = link.replace("twitter", "fxtwitter")

        # Send the modified link as a message
        await message.delete()
        await message.channel.send(f"Posted by {author}: {modified_link}")


# Use regex to match a link starting with "https://tiktok.com/"
    match = re.match(r'(https?:\/\/(?:www\.)?tiktok\.com\/\S+)',
                     message.content)

    if match:
        # Get the matched link
        link = match.group(1)
        author = message.author.name
        # Modify the link to replace "tiktok" with "vxtiktok"
        modified_link = link.replace("tiktok", "vxtiktok")

        # Send the modified link as a message
        await message.delete()
        await message.channel.send(f"Posted by {author}: {modified_link}")

    if message.content.startswith('$hello'):
        await message.channel.send('Whoever summoned me is gay')
        if message.content.startswith('$hello'):
            await message.delete()

    if message.content.startswith('$bruh'):
        await message.channel.send(
            'https://tenor.com/view/bruh-bye-ciao-gif-5156041')
        if message.content.startswith('$bruh'):
            await message.delete()

    if message.content.startswith('$gang'):
        await message.channel.send(
            'https://media.giphy.com/media/cVSWa1PDcToGc/giphy.gif')
        if message.content.startswith('$gang'):
            await message.delete()

    if message.content.startswith('$slap'):
        await message.channel.send(
            'https://tenor.com/view/el-risitas-come-on-come-on-man-mustache-serious-gif-17362553'
        )
        if message.content.startswith('$slap'):
            await message.delete()

    if message.content.startswith('$pain'):
        await message.channel.send(
            'https://tenor.com/view/hide-the-pain-harold-gif-10575677')
        if message.content.startswith('$pain'):
            await message.delete()

    # if message.content.startswith('e'):
    #await message.channel.send('ko e ble')    #no way he brought back
    #you dirsies your last dirst
    #you e'd your last e
    #

    if message.content.startswith('dirst'):
        await message.channel.send('nedirsies daudz te ja')

    if message.content.startswith('pips'):
        await message.channel.send('pats ne labaks')

keep_alive()
client.run(TOKEN)
#ahujel ble, actual threats ble, jo teoretisk jus redzet nevarat lkm
#omegalul haha, nja .env laikam tik creatoram redzams
