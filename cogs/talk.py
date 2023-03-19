from disnake.ext import commands
from main import channel_dic
import time
import random

class Messaging(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channel_dic = channel_dic
    

    # Sends a message to a single user
    @commands.command()
    async def msgdm(self, ctx, channel_name: str, *, message: str):
        try:
            dmreceiver = await self.client.fetch_user(self.channel_dic[channel_name])
            await dmreceiver.send(message)
            await ctx.send('oke')
        except:
            await ctx.send("e")

    # Sends a message to a specific channel
    @commands.command()
    async def msg(self, ctx, channel_name: str, *, message: str):
        try:
            channel = self.client.get_channel(self.channel_dic[channel_name])
            await channel.send(message)
        except:
            await ctx.send("can't")
            
    # Rates argument from a scale of 1 to 10
    @commands.command()
    async def rate(self, ctx, *, message: str):
        try:
            await ctx.send('i give ' + message + ' a ' + str(random.randint(1,10)) + '/10')
        except:
            await ctx.send("can't")
    


class Hello(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Initialized message in the terminal
    @commands.Cog.listener()
    async def on_ready(self):
        print('lets do this')

    # Message Listener
    @commands.Cog.listener()
    async def on_message(self, ctx):
        # Exclude Mosor-BOT
        if ctx.author.bot and not str(ctx.author) == 'Mosor-BOT#4095':
            return
        
        # Says Good Morning back to the user
        if ctx.content.lower().startswith('gm'):
            print('Gm detected')
            await ctx.channel.send('Gm, ' + ctx.author.name)
        
        # Says "waw" when hearing her name
        if 'serval' in ctx.content or 'waw' in ctx.content:
            await ctx.channel.send('waw')
        
        # displays DM replies in the terminal
        if ctx.guild == None:
            print(f'{ctx.author}[DM]: {ctx.content}')
        
        # displays server messages in the terminal
        else:
            print(f'{ctx.author}[{ctx.channel}]: {ctx.content}')
            
    # Sends a funny gif
    @commands.command()
    async def die(self, ctx):
        print(ctx.guild.owner_id)
        if ctx.author.id == ctx.guild.owner_id:
            await ctx.send('https://tenor.com/view/dies-cat-dead-died-gif-13827091')
            await self.client.close()
        else:
            await ctx.send('impostor')

    # Ping Pong
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('..pong')
    
    # Sends back a Vince gif
    @commands.command()
    async def silence(self, ctx):
        await ctx.send('https://tenor.com/view/vince-mcmahon-order-gif-20615354')


class Cleanup(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    # Counts the number of times a word has been said in the last n messages
    @commands.command()
    async def count(self, ctx, *, word: str):
        messages = await ctx.channel.history(limit=2000).flatten()
        messagecount = 0
        for msg in messages:
            if word in msg.content:
                messagecount += 1
        await ctx.send(word + ' has been said ' + str(messagecount) + ' times')
    
    # Deletes messages containing a certain word
    @commands.command()
    async def escapeplan(self, ctx, *, word: str):
        def is_word(m):
            return word.lower() in m.content
        try:
            await ctx.channel.purge(limit=20, check=is_word)
        except:
            await ctx.send('wah')


def setup(client):
    client.add_cog(Hello(client))
    client.add_cog(Messaging(client))
    client.add_cog(Cleanup(client))