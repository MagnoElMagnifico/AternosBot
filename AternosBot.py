import discord
from JsonManager import read
from AternosAPI import *

#### Path to your .json file with required data ####
JSON = "data.json"

# Create the required objects
data   = read(JSON)
bot    = discord.Client()
server = AternosServer(data["aternos-session"], data["aternos-server"])

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

    print(
f"""
-------------------------------------------------
  message: {message.content}
  arg: {message.content.lower().replace("%ab ", "")}
  author: {message.author}
  message.channel: {message.channel}
-------------------------------------------------
""")

    HELP_INFO = f""" Working on it! """

    #### BOT OPTIONS ####
    try:
      # Sends a test message
      if arg == "test":
        await message.channel.send("{0.mention} Test concluded!".format(message.author))

      # Disconnects from the guild/server
      elif arg == "close":
        await message.channel.send("{0.mention} :ok_hand:".format(message.author))
        await bot.close()

      # Sends all the information of the server
      elif arg == "get":
        await message.channel.send(
          "{0.mention}".format(message.author)         +
          "\nName: "     + server.get_server_name()    +
          "\nStatus: "   + server.get_online_status()  +
          "\nPlayers: "  + server.get_online_players() +
          "\nVersion: "  + server.get_server_version() +
          "\nSoftware: " + server.get_server_software())

      # Sends the minecraft server IP
      elif arg == "server name":
        await message.channel.send("{0.mention} ".format(message.author) + server.get_server_name())

      # Sends the status of the server (online, offline, loading, on queue)
      elif arg == "status":
        await message.channel.send("{0.mention} ".format(message.author) + server.get_online_status())

      # Sends the online players of the server (online/max)
      elif arg == "players":
        await message.channel.send("{0.mention} ".format(message.author) + server.get_online_players())

      # Sends the server sofware
      elif arg == "version":
        await message.channel.send("{0.mention} ".format(message.author) + server.get_server_version())

      # Sends the server software
      elif arg == "software":
        await message.channel.send("{0.mention} ".format(message.author) + server.get_server_software())

      # Sends the server queue status (your place/last place)
      elif arg == "queue number":
        try:
          await message.channel.send("{0.mention} ".format(message.author) + server.get_queue_number())
        except UnexpectedError as e:
          await message.channel.send("{0.mention} Cannot load the queue data because the server it is not on the queue".format(message.author))

      # Sends the server queue status (time left)
      elif arg == "queue time":
        try:
          await message.channel.send("{0.mention} ".format(message.author) + server.get_queue_time_left())
        except UnexpectedError as e:
          await message.channel.send("{0.mention} Cannot load the queue data because the server it is not on the queue".format(message.author))

      # Shows up some information about the bot
      elif arg == "help":
        await message.channel.send(HELP_INFO)
      else:
        await message.channel.send(HELP_INFO)
    except AternosError as e:
      await message.channel.send("ERROR... ADMIN check the console!")
      print(e)

bot.run(data["bot-token"])
