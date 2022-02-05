from datetime import datetime
from configs import config


def logger(command, user, status):
    if config.logging:
        if status:
            status = "Success"
        else:
            status = "Error"

        print(f'[{today_date_and_time()}] /{command} <{status}> {user}')


def today_date_and_time():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")
