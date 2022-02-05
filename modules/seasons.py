from configs import config
from random import randint


def name_to_database(name):
    if name == "all":
        season = randint(0, len(config.database)-1)
        return [config.database[season][1], config.database[season][2]]
    else:
        for i in config.database:
            if i[0] == name:
                return [i[1], i[2]]
        return 0
