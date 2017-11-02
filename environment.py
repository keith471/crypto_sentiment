from os.path import join, dirname
from dotenv import get_variable

class Environment(object):

    ##
    # Constructor to load .env
    ##
    def __init__(self, env_str):
        if env_str != "test":
            env_str = "local"
        print('Using environment - %s' % env_str)
        dotenv_path = join(dirname(__file__), 'environments/.env-' + env_str)
        self.DB_HOST = get_variable(dotenv_path, "DB_HOST")
        self.DB_NAME = get_variable(dotenv_path, "DB_NAME")
        self.DB_USERNAME = get_variable(dotenv_path, "DB_USERNAME")
        self.DB_PASSWORD = get_variable(dotenv_path, "DB_PASSWORD")
