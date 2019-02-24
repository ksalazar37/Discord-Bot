# Discord-Bot

![PyPI](https://img.shields.io/badge/python-3.4--3.6-5ba7e5.svg)
![PyPI](https://img.shields.io/badge/code_size-24.56_kB-51c0d1.svg)
![PyPI](https://img.shields.io/badge/scripts-6-72b73a.svg)
<br>
![PyPI](https://img.shields.io/badge/API-Wolfram_Alpha-e27177.svg)
![PyPI](https://img.shields.io/badge/API-Reddit-ed8653.svg)
![PyPI](https://img.shields.io/badge/applications-Discord-779bce.svg)


<br>
A multifunctional discord bot built from the discord.py wrapper that: <br>
- Sends answers to user queries from Wolfram Alpha using the Wolfram Alpha API <br>
- Operates the Reddit API to send text and image posts to a user from any defined subredit <br>
- Plays music in discord voice channels <br>
- Performs other various interactive tasks with discord users
<br><br><br>


## I. Set Up
### Installation
Installation of discord wrapper and API clients can be completed using the following pip install commands:
```
pip install -U discord.py[voice]   
pip install wolframalpha 
pip install praw  
pip install requests
```
###  Importing Libraries for each script
```
import discord
from discord.ext import commands
import asyncio
import random
import praw
```
 <br><br> <br><br>
## II. Built With
* [Python 3](https://www.python.org/downloads/release/python-367/) - Python version 3.6.7
* [Discord](https://discordapp.com/developers/applications/) - Discord Developers, uset to create application and bot to connect to Discord Application
* [Discord.py API Wrapper](https://github.com/Rapptz/discord.py) - API wrapper for discord bot written in Python
* [Wolfram Alpha](https://www.wolframalpha.com/) - Wolfram Alpha
* [Wolfram Alpha API](https://products.wolframalpha.com/api/) - API wrapper to allow for Wolfram Alpha queries in any application with scripts in any language
* [Reddit](https://www.reddit.com/prefs/apps) - connects the Discord bot to reddit
* [Reddit API Wrapper](https://github.com/praw-dev/praw) - API wrapper for reddit scripts written in Python


 <br><br> <br><br>
 
## III. Examples of Bot Commands
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Wolfram_Alpha_logo.svg/500px-Wolfram_Alpha_logo.svg.png)](https://www.wolframalpha.com/) <br>


### Wolfram Alpha
`!wolf < query >`
<br> <br>
***Query examples include:***
<br> 
***Mathematics & Statistics*** <br>
  `!wolf integrate x^2 sin^3 x dx` <br>
  `!wolf annulus, inner radius=2, outer radius=5 ` <br>
  `!wolf linear fit {1.3, 2.2},{2.1, 5.8},{3.7, 10.2},{4.2, 11.8}'` <br> <br>
  
***Plotting - Returns an image of graph*** <br>
  ` !wolf plot sin x tan y` <br> 
  `!wolf 3d parametric plot (cos u, sin u + cos v, sin v), u=0 to 2pi, v=0 to 2pi` <br>
   `!wolf plot (x^2 + y^2 -1)^3 - x^2y^3 = 0 ` <br>
  `!wolf graph sin t + cos (sqrt(3)t)` <br><br>
  
  
***Science & Technology*** <br>
  `!wolf Kepler's third law, 4 solar masses, 5 Earth masses, 2.5 AU` <br>
  `!wolf octane + O2 -> water + CO2` <br>
  `!wolf Apollo 11` <br>
  `!wolf 10 miles + 14 kilometers` <br>
  `!wolf convert 55 mph to SI` <br><br>
  

***Society & Culture*** <br> 
  `!wolf world gdp per capita` <br>
  `!wolf Canada healthcare expenditures` <br>
  `!wolf Human Development Index` <br>
  `!wolf Who was Gandalf the Grey?` <br>
  `!wolf Who wrote Stairway to Heaven?` <br>
  `!wolf heart rate 50yo male, resting hr=60bpm` <br> <br>
  
***General*** <br>
 ` !wolf weather forecast ` <br>
  `!wolf heat index Abu Dhabi` <br>
  `!wolf price of gasoline in Houston` <br>
  `!wolf flights from LAX to NYC ` <br>
  `!wolf distance from Rome to Naples in kilometers` <br>
 
 <br><br> <br><br>
### Reddit
[![](https://3j6x6z2bx1qq1aawwt3b6y0a-wpengine.netdna-ssl.com/wp-content/uploads/post/reddit-logo-390x142.png)](https://www.reddit.com/) <br>
`!< name of pre-defined subreddit to pull post from, without "r/" > < number of posts to pull >`
 <br> <br>

 
Subreddit examples include: <br> <br>
`!science` <br>
`!worldnews` <br>
`!programming` <br>
`!art` <br>
`!todayilearned`  
<br><br> <br><br>

### Basic Commands using On_Message
`!hello` <br>
`!hi` <br>
`!test` <br>
`!square` < number > <br>
`!8ball `
