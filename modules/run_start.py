from configs import config
from configs.config import episodes_database
import csv


def load_database():
    try:
        with open(episodes_database) as csvfile:
            parsed_csv = csv.reader(csvfile, delimiter=";")
            for row in parsed_csv:
                config.database.append(row)

    except FileNotFoundError:
        return 0
