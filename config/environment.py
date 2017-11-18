from os.path import join, dirname
from dotenv import get_variable
import logging
import sys

class Environment(object):
    def __init__(self, env_str):
        if env_str != "test":
            env_str = "local"
        print('Using environment - %s' % env_str)
        dotenv_path = join(dirname(__file__), 'environments/.env-' + env_str)

        # setup db info
        self.DB_HOST = get_variable(dotenv_path, "DB_HOST")
        self.DB_NAME = get_variable(dotenv_path, "DB_NAME")
        self.DB_USERNAME = get_variable(dotenv_path, "DB_USERNAME")
        self.DB_PASSWORD = get_variable(dotenv_path, "DB_PASSWORD")

        # setup twitter oauth stuff
        self.APP_KEY = get_variable(dotenv_path, "APP_KEY")
        self.APP_SECRET = get_variable(dotenv_path, "APP_SECRET")
        self.TOKEN = get_variable(dotenv_path, "TOKEN")
        self.TOKEN_SECRET = get_variable(dotenv_path, "TOKEN_SECRET")

        # setup logging
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)
