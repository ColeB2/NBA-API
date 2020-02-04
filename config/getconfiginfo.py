'''
getconfiginfo.py - functions used to grab information from the config file
'''
import os
import configparser

config_folder = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(config_folder, 'config.ini')

def get_season():
    #config = configparser.ConfigParser()
    config = configparser.RawConfigParser()
    config.read(config_path)

    season_year = config.get('Values', 'season')
    return season_year

def get_team():
    config = configparser.RawConfigParser()
    config.read(config_path)

    team = config.get('Favourite Team', 'team')
    return team

def get_init_config():
    config = configparser.RawConfigParser()
    config.read(config_path)

    is_configured = config.get('Initial Config', 'config')
    return is_configured




if __name__ == '__main__':
    x = get_season()
    print(x)

    y = get_team()
    print(y)

    z = get_init_config()
    print(z)
