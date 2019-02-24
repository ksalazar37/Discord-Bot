import discord
import random
import asyncio
import praw
from discord.ext import commands

# Reddit API, attain ID 
reddit = praw.Reddit(client_id='id',
                     client_secret='clsecret',
                     user_agent='agent')

# create Reddit class with functions and commands 
class Reddit:
    def __init__(self, bot):
        self.bot = bot

        # Starts loops so that it will run constantly while the bot.py is running
        self.bot.loop.create_task(self.background_task())
        self.bot.loop.create_task(self.dm_task())

    async def background_task(self):
        await self.bot.wait_until_ready()

        # The channel id - Must have developer mode on in discord
        channel = discord.Object(id='cID')
        # Bot does not start for 1 hour(3600 seconds)

        await asyncio.sleep(3600)
        while not self.bot.is_closed:
            # while the bot.py is still running, do this

            # Decides what subreddit you are going to
            mes = reddit.subreddit('worldnews').hot()

            # picks a post from the top 20
            post_to_pick = random.randint(1, 20)

            # Goes to /r/worldnews reddit and grabs a random post from the hot section
            for i in range(0, post_to_pick):
                submission = next(x for x in mes if not x.stickied)
            await self.bot.send_message(channel, submission.url)

            # sleeps for 1 hour then repeats
            await asyncio.sleep(3600)


    # allows for the prefixes (! and ?) set in bot.py to work to call this function
    @commands.command(pass_context=True)
    async def science(self):
        # Decides what subreddit you are going to
        pup = reddit.subreddit('science').hot()

        # picks a post from the top 20 of the science subreddit 
        post_to_pick = random.randint(1, 20)

        for i in range(0, post_to_pick):
            submission = next(x for x in pup if not x.stickied)
        await self.bot.say(submission.url)
  
    # this is the same block of code used for accessing a subreddit post
    # The command is any_subreddit which will be called by the user in discord 
    @commands.command(pass_context=True)
    async def any_subreddit(self):
        any_subreddit = reddit.subreddit('any_subreddit').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in any_subreddit if not x.stickied)
        await self.bot.say(submission.url)


def setup(bot):
    bot.add_cog(Reddit(bot))
    print('Reddit has loaded')
