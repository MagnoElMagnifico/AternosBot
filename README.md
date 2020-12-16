# AternosBot
[Discord](https://discord.com) bot to manage a minecraft server in [Aternos](https://aternos.org).
By [Magno The Magnific](https://github.com/MagnoElMagnifico "me lol").

## Features
+ Currently:
  - Connect with discord
  - Show information about the bot itself typing `%ab` or `%ab help`
  - Respond to messages mentioning people with `%ab test`
  - Close the bot from discord with `%ab close`
+ **Main achivements**:
  - Open and close the server
  - Get the server status: `online`/`offline`, people online, etc.

## Set up
You will have to host yourself this bot. To do this you can check the [Discord Developer Portal](https://discord.com/developers/docs/intro), [The Coding Train video](https://www.youtube.com/watch?v=ibtXXoMxaho&t) or try to follow these poorly-written instructions:

+ Go to [your apps](https://discord.com/developers/applications) and create one. Fill the gaps with the required information.
+ Now go to your bots (on the side options) and create a bot linked to that application.
+ Copy the `TOKEN`.
+ Finally, to be able to conect your application to your discord server, use the following link with the `CLIENT ID` of your application.

  ```
    https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot
  ```

This should make the bot join to your discord server, but it would appear as disconnected. Let's see how to turn it on.
**Note**: You can use the [official aternos icon](aternos-icon.png) for your bot.

+ Now, to set up the bot, just clone this repository with `git` from the `CMD`: `git clone https://github.com/MagnoElMagnifico/AternosBot` or download the `.zip` file [here](https://github.com/MagnoElMagnifico/AternosBot/archive/main.zip) and extract the source code.
+ [Python](https://www.python.org/downloads/) is required to run this program, so just type `python AternosBot.py` on the command line.
+ If you get some importing errors (`ModuleNotFoundError`), try installing those modules with:

  ```
    pip install discord.py
  ```

+ To link this program with the actual discord's bot, create a `data.json` file on the root folder of this project (or change its path in [AternosBot.py](AternosBot.py) line 5) with the following structure and implement the `TOKEN` you have copied from the beginning.

  ```
    {
      "bot-token": "PASTE_HERE"
    }
  ```

## Modules used - Requirements
+ [BeatifulSoup](https://crummy.com/software/BeautifulSoup/)
+ [Requests](https://pypi.org/project/requests/)
+ [Discord.py](https://pypi.org/project/discord.py/)

## Developer useful links
+ https://discordpy.readthedocs.io/en/latest/api.html
+ https://realpython.com/how-to-make-a-discord-bot-python/

## Contact information
+ marcosgranja317@gmail.com
