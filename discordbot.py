import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}!')

@client.command()
async def join_channel(ctx, channel: discord.TextChannel):
    await channel.join()

client.run('MTA1MTUwNju0MjQwODYzNDQyOA.GAgflK.QQO7VTBE3xiaxDPfqc_jvpnjjMnDFOD20I1bMg')
