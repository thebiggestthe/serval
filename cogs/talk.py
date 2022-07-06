from disnake.ext import commands
from main import channel_dic
import time

class Messaging(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channel_dic = channel_dic

    @commands.command()
    async def msgdm(self, ctx, channel_name: str, *, message: str):
        try:
            dmreceiver = await self.client.fetch_user(self.channel_dic[channel_name])
            await dmreceiver.send(message)
            await ctx.send('oke')
        except:
            await ctx.send("e")

    @commands.command()
    async def msg(self, ctx, channel_name: str, *, message: str):
        try:
            channel = self.client.get_channel(self.channel_dic[channel_name])
            await channel.send(message)
        except:
            await ctx.send("can't")
            
    @commands.command()
    async def spell(self, ctx, *, motd):
        try:
            for motd_line in motd.replace(" ", ""):
                async with ctx.typing():
                    await ctx.send(motd_line)
                    time.sleep(1)
        except:
            await ctx.send('sowwy')


class Hello(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('lets do this')

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot and not str(ctx.author) == 'Mosor-BOT#4095':
            return
        
        if ctx.content.lower().startswith('gm'):
            print('Gm detected')
            await ctx.channel.send('Gm, ' + ctx.author.name)
        
        if 'serval' in ctx.content or 'waw' in ctx.content:
            await ctx.channel.send('waw')
        
        if ctx.guild == None:
            print(f'{ctx.author}[DM]: {ctx.content}')
        
        else:
            print(f'{ctx.author}[{ctx.channel}]: {ctx.content}')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('..pong')
    
    @commands.command()
    async def debug(self, ctx):
        await ctx.send(str(ctx.author))

    @commands.command()
    async def silence(self, ctx):
        await ctx.send('https://tenor.com/view/vince-mcmahon-order-gif-20615354')


class Escape(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def count(self, ctx, *, word: str):
        messages = await ctx.channel.history(limit=2000).flatten()
        messagecount = 0
        for msg in messages:
            if word in msg.content:
                messagecount += 1
        await ctx.send(word + ' has been said ' + str(messagecount) + ' times')
    
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
    client.add_cog(Escape(client))