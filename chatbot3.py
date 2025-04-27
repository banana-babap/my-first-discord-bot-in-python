import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # Required to read message content
bot = commands.Bot(command_prefix="!", intents=intents)

# Event that triggers when the bot is ready and connected
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Command to respond with "Hello!"
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

# Command to respond with "Ping!" when someone sends "!ping"
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Start the bot using the token you got earlier
bot.run('MTM2NjA2MDQ4MDQwOTUwMTcyOA.G0TOJO._zt5pZOQtOdRbhSKCBFdzmgQI-1HlSA6YL5G28')

