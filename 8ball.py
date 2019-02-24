import random

from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "Token"

client = Bot(command_prefix=BOT_PREFIX)

# description 
@client.command(name = "8ball",
                description="Answers a yes/no question.",
                brief = "Answers from the beyond.",
                aliases= [ "eight_ball", "eightball", "8-ball"],
                pass_context = True)

async def eight_ball(context):
    possible_responses = [
        "It is clearly certain",
        "It is obviously true",
        "Without a doubt",
        "You may rely on it",
        "Outlook good",
        "Yes",
        "Cannot predict now",
        "Concentrate and ask again",
        "It is not obvious",
        "Don't count on it",
        "Sources from the beyond say no",
        "Outlook not so good.",
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)




@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


client.run(TOKEN)
