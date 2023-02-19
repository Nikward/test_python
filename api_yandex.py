import configparser

import requests

def get_token_ya():
    config = configparser.ConfigParser()
    config.read("setting.ini")
    return config['yandex_api']['ya_token']


