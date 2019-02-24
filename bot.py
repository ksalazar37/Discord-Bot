# main discord bot script
# initiates all other script with ran

from discord.ext import commands
from discord.ext.commands import Bot

# list of names of extensions of bot
bot_extensions=["wolf_alpha", "reddit", "play_music", "eight_ball","message_reply"]
bot = commands.Bot(command_prefix='!')

# prefix before entering a command 
BOT_PREFIX = ("?", "!")
TOKEN = "token"

client = Bot(command_prefix=BOT_PREFIX)

# run
if __name__ == "__main__":
    for extension in bot_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__,e)
            print('failed to load ext'.format(extension, exc))

bot.run("TOKEN")
