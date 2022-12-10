import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}!')

@client.command()
async def join_channel(ctx, channel: discord.TextChannel):
    await channel.join()

client.run('MTA1MTIxNDIzODM4NDkyMjYzNA.Gcb0Ga.fCM4gl4m0UH_4qXLotmcWj53rEElbpywYTWXrc')