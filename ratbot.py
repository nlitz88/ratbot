import discord
from discord.ext import commands
import os

# Create the bot instance and configure it.
ratbot = commands.Bot(intents=discord.Intents.default(), command_prefix="*")

# Run ratbot with the token provided as an environment variable.
ratbot.run(os.getenv("TOKEN"))