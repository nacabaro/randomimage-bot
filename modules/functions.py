from modules.seasons import *
import os
import secrets


def random_episode_name(arg):
    season_database = name_to_database(arg)[1]
    if not season_database == 0:
        with open(season_database) as episodeDatabase:
            episodes = episodeDatabase.readlines()

        episode = secrets.choice(episodes)
        episode = episode.strip("\n")

        return episode
    else:
        return -1


def convert_episode(episode):
    name = secrets.token_hex(32)

    random_minute = secrets.randbelow(23)
    if random_minute > 22:
        random_second = secrets.randbelow(30)
    else:
        random_second = secrets.randbelow(60)

    random_ms = secrets.randbelow(1000)
    random_time = str(random_minute) + ":" + str(random_second).zfill(2) + "." + str(random_ms).zfill(3)

    os.system(f'''ffmpeg -hide_banner -loglevel error -ss {random_minute}:{random_second}.{random_ms} -i "{episode}" -vframes 1 /tmp/{name}.png''')

    return [f'{name}.png', random_time]


def delete_image(name):
    os.remove(f'/tmp/{name}')
