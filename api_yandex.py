import configparser
import os.path
import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'


def get_token_ya():
    config = configparser.ConfigParser()
    path = os.path.abspath("setting.ini")
    config.read(path)
    token = config['yandex_api']['ya_token']
    return token


def create_folder(token, name_folder):
    params = {'path': name_folder}
    headers = {'Content-Type': 'application/json',
               'Authorization': token
               }
    create_folder = requests.put(URL, params=params, headers=headers)
    return create_folder.status_code
