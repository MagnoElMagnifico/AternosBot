import discord
from JsonManager import read

#### Path to your .json file with the data ####
JSON = "data.json"

# Create the bot object
bot = discord.Client()

# Prints some debugging information about a message given to the bot
def debug(message):
  print(
f"""
-------------------------------------------------
  message: {message.content}
  arg: {message.content.lower().replace("%ab ", "")}
  author: {message.author}
  message.channel: {message.channel}
-------------------------------------------------
""" )

# Executed when the bot is ready
@bot.event
async def on_ready():
  print(
f"""
------------------ Ready!! ----------------------
  bot: {bot}
  user: {bot.user}
  guilds: {bot.guilds}
-------------------------------------------------
""")

# Executed when sended a message
@bot.event
async def on_message(message):

  # %ab to call the bot
  if message.content.lower().startswith("%ab"):

    # get the arguments given to the bot
    arg = message.content.lower().replace("%ab ", "")
    debug(message)

    HELP_INFO = f"""
Hello, my name is {bot.user} and you can call me messaging **%ab**.
I have this options avaliable:
    · **test** : Respond to messages mentioning people (testing purposes)
    · **close**: I'll leave if you don't need me!
    · **help** : Shows this information
"""

    #### BOT OPTIONS ####
    # Sends a test message
    if arg == "test":
      await message.channel.send("{0.mention} Test concluded!".format(message.author))

    # Disconnects from the guild/server
    elif arg == "close":
      await message.channel.send("{0.mention} :ok_hand:".format(message.author))
      try:
       await bot.close()
      except:
        pass

    # Shows up some information about the bot
    elif arg == "help":
      await message.channel.send(HELP_INFO)
    else:
      await message.channel.send(HELP_INFO)

bot.run(read(JSON)["bot-token"])
