import discord
from discord.ext import commands
import os

Bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('1234567890'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
