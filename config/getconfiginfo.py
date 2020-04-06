"""
getconfiginfo.py - functions used to grab information from the config file,
    exceptions, and quick reset options.
"""
import os
import configparser

config_folder = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(config_folder, 'config.ini')

class ConfigError(Exception):
    pass


def get_info(config_option):
    """Gets the information requested from the config.ini file.

    Args:
        config_option: tuple, with options used in config.ini file.
        *Titles:                 variable values:
        'Values' -- 'config'
        'Team' -- 'team'
        'Initial Config' -- 'season'

    Returns;
        requested value asked for in config_options
        """
    config = configparser.RawConfigParser()
    config.read(config_path)

    return config.get(config_option[0], config_option[1])

def quick_config_reset():
    config = configparser.RawConfigParser()
    config.read(config_path)

    config.set('Initial Config', 'config', 'False')
    with open(config_path, 'w') as configfile:
        config.write(configfile)



if __name__ == '__main__':
    print(f"season: {get_info(('Values', 'season'))}")
    print(f"team: {get_info(('Team', 'team'))}")
    print(f"config: {get_info(('Initial Config', 'config'))}")
