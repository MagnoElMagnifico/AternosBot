# AternosBot
[Discord](https://discord.com) bot to manage a minecraft server in [Aternos](https://aternos.org).
By [Magno The Magnific](https://github.com/MagnoElMagnifico "me lol").

## Features
+ Connect with discord
+ Read the required data from a `.json` file
+ Show information about the bot itself typing `%ab` or `%ab help`
+ Respond to messages mentioning people with `%ab test`
+ Close the bot from discord with `%ab close`
+ Connect with aternos.org and get info about the server:
  - `%ab server name`: Server name
  - `%ab status`: Online status
  - `%ab players`: Online players
  - `%ab version`: Minecraft server version
  - `%ab software`: Minecraft server software
  - `%ab queue`: Position in the queue and estimated time left
  - `%ab queue number`: Position in the queue while starting the server (your position/last position)
  - `%ab queue time`: Estimated time until the server starts
+ **Still in progress**:
  - Open and close the server
  - Send a message periodicly updating the server info
  - List of persons who can interact with the bot

## Set up
See [the set up documentation](documentation/SETUP.md)

## Modules used - Requirements
+ [Python](https://www.python.org/downloads/)
+ [BeatifulSoup](https://crummy.com/software/BeautifulSoup/)
+ [Requests](https://pypi.org/project/requests/)
+ [Discord.py](https://pypi.org/project/discord.py/)

## References and links
+ The [AternosAPI](AternosAPI.py) is based on [Duerocraft's one](https://github.com/Duerocraft/AternosAPI)
+ [Discord.py documentation](https://discordpy.readthedocs.io/en/latest/api.html)
+ [Simple discord.py tutorial](https://realpython.com/how-to-make-a-discord-bot-python/)

## Contact information
+ marcosgranja317@gmail.com
+ Discord name: Magno El Magnífico#6193
