import discord
from discord.ext import commands
import os

#importing music and help cog
from help_cog    import help_cog
from music_cog   import music_cog

# Create the bot instance and configure it.
ratbot = commands.Bot(intents=discord.Intents.default(), command_prefix="*")

# Run ratbot with the token provided as an environment variable.
ratbot.run(os.getenv("TOKEN"))
#
ratbot.add_cog(music_cog(ratbot))
ratbot.add_cog(help_cog(ratbot))

#
ratbot.run(os.getenv("TOKEN"))