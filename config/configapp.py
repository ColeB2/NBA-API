'''
configapp.py - A bunch of functions used in configuring the main app to work
with the users favourite team
'''
import configparser
import datetime
import json
import os
import sys
import urllib.request

sys.path.append(os.path.abspath(os.path.join('..', 'api_functions')))
sys.path.append(os.path.abspath(os.path.join('.', 'api_functions')))
from nbateam import get_team_data, TeamInfo
from functions import get_data

config_folder = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(config_folder, 'config.ini')


class ConfigureApp(object):
    def __init__():
        self.TI = TeamInfo()
        self.config = configparser.RawConfigParser()
        #self.config.read(config_path)

    def configure(self):
        self.config_settings()
        self.set_default_season()
        self.check_season()

    def config_settings():
        config = configparser.RawConfigParser()
        config.read(config_path)
        is_configured = config.get('Initial Config', 'config')
        if is_configured == 'False':
            set_presets(config)

    def team_select():
        """TODO: Use team module to get team info. at least use the get data func"""
        for team in self.TI.standard:
            if team['isNBAFranchise'] == True:
                print(f"{team['tricode']}: {team['fullName']}")
        print(f"Input your teams tricode, ex ORL, PHI, PHX etc:")
        team = input()
        return team


    def set_presets(parser):
        '''
        set_presets(parser)
        Function used by config_settings to set presets of config.ini file
        '''
        TI = TeamInfo()
        fave_team = team_select()
        my_team = get_team_url(fave_team)
        parser.set('Team', 'team', str(my_team))
        parser.set('Initial Config', 'config', 'True')
        parser.set('Values', 'season', set_default_season())
        with open('config.ini', 'w') as configfile:
            parser.write(configfile)


    def set_default_season():
        '''Sets season default to the year of current season, done so for when
        season is left blank in any function that reqeuires it

        TODO:
        use get_data funcs, '''
        url = 'http://data.nba.net/10s/prod/v1/today.json'
        get_data(url)
        season = get_data(url)['teamSitesOnly']['seasonYear']

        return str(season)


    def set_default_date():
        '''Sets date default date to proper format, done for functions that
        require a date in the url, and one isn't given'''
        pass



    def check_season():
        '''
        Checks to make sure the season setting is correct
        '''
        config = configparser.ConfigParser()
        config.read(config_path)
        current_season = set_default_season()
        season_check = config.get('Values', 'season')
        if season_check != current_season:
            config.set('Values', 'season', current_season)
            with open('config.ini', 'w') as configfile:
                config.write(configfile)




if __name__ == '__main__':
    #configure_app()
    config = configparser.ConfigParser()
    config.read(config_path)
    print(config.sections())
    for item in config.sections():
        for key in config[item]:
            print(key)
