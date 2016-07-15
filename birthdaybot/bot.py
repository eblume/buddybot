# -*- coding: utf-8 -*-

import os
import requests
from datetime import date
from dotenv import load_dotenv
from slacker import Slacker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise EnvironmentError(error_msg)

SLACK_API_KEY = get_env_variable('SLACK_API_KEY')

slack = Slacker(SLACK_API_KEY)

BIRTHDAYS = [
    {
        'user': "erich",
        'name': "Erich",
        'date': (12, 13),
    },
    {
        'user': "phildini",
        'name': "Phil",
        'date': (8, 14),
    },
    {
        'user': "kkarinhawley",
        'name': "Karin",
        'date': (11, 19),
    },
    {
        'user': "arctansusan",
        'name': "Susan",
        'date': (11, 19),
    },
    {
        'user': "elzilrac",
        'name': "Allison",
        'date': (11, 27),
    },
    {
        'user': "nicholle",
        'name': "Nicholle",
        'date': (2, 9),
    },
]

def main():
    today = date.today()
    for birthday in BIRTHDAYS:
        date = date(today.year, birthday['date'][0], birthday['date'][1])
        if today == date:
            message = ":cake::cake::cake: HAPPY BIRTHDAY {}!!!:cake::cake::cake: ".format(
                birthday['name'].upper())
            send_buddybot_message(message, channel='general')


def send_buddybot_message(message, attachments=None, user=None, channel=None):
    if user:
        message_response = slack.chat.post_message(
            "@{}".format(user),
            message,
            attachments=attachments,
            username="BuddyBot",
            icon_emoji=":heart:",
        )
    if channel:
        message_response = slack.chat.post_message(
            "#{}".format(channel),
            message,
            attachments=attachments,
            username="BuddyBot",
            icon_emoji=":heart:",
        )


if __name__ == '__main__':
    main()
