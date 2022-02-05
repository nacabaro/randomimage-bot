#!/usr/bin/python3
from modules.commands import bot
from modules.run_start import *
from configs import config


print("Loading database...")
if load_database() == 0:
    print("There was an error loading the database, CSV file not found.")
else:
    print("Database loaded.")

bot.run(config.token)
