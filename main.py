from keep_alive import keep_alive
import os
import discord
from datetime import datetime
import re
from discord.ext.commands import Bot
from dotenv import load_dotenv

intents = discord.Intents.default(
)  # Create a new instance of the Intents class
intents.messages = True  # Adjust the intents based on your bot's requirements
intents.presences = True
intents.message_content = True

#aljooo bljaaaaats
#shadap
# yes honey :(
client = discord.Client(
  intents=intents
)  # Pass the intents argument when creating the client instance

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('DISCORD_PREFIX')
client = discord.Client(intents=intents)

client = Bot(command_prefix=list(PREFIX), intents=intents)

x = datetime.now()  #console time log
x = str(x)

user_messages = {
}  # Create a dictionary to store user messages and their corresponding converted links


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name='That Dawg in Me')
                               )

  for guild in client.guilds:
    if guild.name == GUILD:
      break
  print('Bot started at ' + x)
  print(f'{client.user} has connected to Discord!:\n'
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        f'Sometimes Life is Pain\n')


# Create a dictionary to store user messages and their corresponding converted links


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
    modified_link = link.replace("instagram", "d.ddinstagram")
    # Extract the text part before and after the link
    #text_before_link = message.content.split(link)[0].strip()
    text_after_link = message.content.split(link)[-1].strip()

    # Send the modified link as a message
    await message.delete()
    #original_message, modified_link = user_messages[author]
    await message.channel.send(
      f"Posted by {author}: **{text_after_link}**\n {modified_link}", silent=True)

# Use regex to match a link starting with "https://twitter.com/"
  match = re.match(r'(https:\/\/twitter\.com\/\S+)', message.content)

  if match:
    # Get the matched link
    link = match.group(1)
    author = message.author.name
    # Modify the link to replace "twitter" with "bettertwitfix -> https://github.com/dylanpdx/BetterTwitFix"
    modified_link = link.replace("twitter", "fixvx")
    # Extract the text part before and after the link
    #text_before_link = message.content.split(link)[0].strip()
    text_after_link = message.content.split(link)[-1].strip()
    # Send the modified link as a message
    await message.delete()
    await message.channel.send(
      f"Posted by {author}: **{text_after_link}**\n {modified_link}", silent=True)


# Use regex to match a link starting with "https://tiktok.com/"
  match = re.match(r'(https?:\/\/(?:www\.)?tiktok\.com\/\S+)', message.content)

  if match:
    # Get the matched link
    link = match.group(1)
    author = message.author.name
    # Modify the link to replace "tiktok" with "vxtiktok"
    modified_link = link.replace("tiktok", "vxtiktok")
    # Extract the text part before and after the link
    #text_before_link = message.content.split(link)[0].strip()
    text_after_link = message.content.split(link)[-1].strip()
    # Send the modified link as a message
    await message.delete()

    await message.channel.send(
      f"Posted by {author}: **{text_after_link}**\n {modified_link}", silent=True)
    
# Use regex to match a link starting with "https://x.com/" (temp fix)
  match = re.match(r'(https?:\/\/(?:\.)?x\.com\/\S+)', message.content)
  if match:
    # Get the matched link
    link = match.group(1)
    author = message.author.name
    # Modify the link to replace "x" with "BetterTwitFix -> https://github.com/dylanpdx/BetterTwitFix"
    modified_link = link.replace("x", "fixvx")
    # Extract the text part before and after the link
    #text_before_link = message.content.split(link)[0].strip()
    text_after_link = message.content.split(link)[-1].strip()
    # Send the modified link as a message
    await message.delete()

    await message.channel.send(
      f" Posted by {author}: **{text_after_link}**\n {modified_link}", silent=True)

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
