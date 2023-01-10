import asyncio
import discord
from discord.ext import commands
import os

#importing music and help cog
from help_cog import help_cog
from music_cog import music_cog
# Create the bot instance and configure it.
ratbot = commands.Bot(intents=discord.Intents.all(), command_prefix="?")
#removes default help commands
ratbot.remove_command("help")

# Run ratbot with the token provided as an environment variable.


async def ratbot_setup(bot):
    """This sets up the music cog and the help cog"""
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))
    

asyncio.run(ratbot_setup(ratbot))

ratbot.run(os.getenv("TOKEN"))