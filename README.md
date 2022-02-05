# RandomImage Discord Bot
A Discord bot that will screenshot video frames at random timestamps of videos provided to it and will send to your Discord server. 

# Requirements
So far this bot has been tested on Linux, as the bot needs access to write to the /tmp folder and assumes you have ffmpeg installed onto your path, requires ffmpeg and discord.py to work. 

# How it works
This bot, when invoked, will generate a random timestamp, pass that timestamp to ffmpeg, which screenshots the frame on that timestamp, then sends it to the discord channel it was invoked on.
This bot has four commands:
- /randomframe, which sends a random frame from between all the seasons provided to the bot.
- /randomfromseason <season alias>, which sends a random frame from any episode of the season provided through the argument.
- /help, which shows all the commands.
- /version, shows bot version.

# Setting it up
To set the bot up:
1. Create a Discord token from the Discord Developer Portal.
2. Edit configs/config.py and add obtained Discord token to the token variable.
3. Edit database.csv file according to the syntax from LAYOUT.txt, contained within the same folder.
4. Add list of episodes to seasons folder.
5. Run.

Optionally, a systemd config file has been provided in order to set it up at boot.
  
# Extra
Detailed information about setting the bot up has been provided in the seasons/ and the config/ folders.
