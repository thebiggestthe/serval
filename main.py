import os
import json
import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True
intents.presences = True

client = commands.Bot(intents=intents, command_prefix='..')


with open('data/token.json') as f:
    token_dic = json.load(f)

with open('data/channels.json') as f:
    channel_dic = json.load(f)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token = token_dic["serval"]

client.run(token)
