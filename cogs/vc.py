import disnake
from disnake.ext import commands

class Voice(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def join(self, ctx):
        print(ctx.channel)

def setup(client):
    client.add_cog(Voice(client))