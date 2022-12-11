import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}!')

@client.command()
async def join_channel(ctx, channel: discord.TextChannel):
    await channel.join()

client.run('MTA1MTUwNjU0MjQwODYzNDQyOA.GAgflK.QQO7VTBE3x1axDPFqc_jvpnjjMnDFOD2OI1bMg')
