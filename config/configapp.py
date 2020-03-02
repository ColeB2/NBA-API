'''
configapp.py - A bunch of functions used in configuring the main app to work
with the users favourite team
'''
import configparser
import json
import os
import urllib.request
#from api_functions.nbateam import get_team_url
import datetime

config_folder = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(config_folder, 'config.ini')

def config_settings():
    config = configparser.RawConfigParser()
    config.read(config_path)
    is_configured = config.get('Initial Config', 'config')
    if is_configured == 'False':
        set_presets(config)


def team_select():
    """TODO: Use team module to get team info. at least use the get data func"""
    url = 'http://data.nba.net/prod/v2/2019/teams.json'
    with urllib.request.urlopen(url) as nba_url:
        data = json.loads(nba_url.read().decode())
        x = data['league']
        y = x['standard']


        for team in y:
            if team['isNBAFranchise'] == True:
                print(team['tricode'], end=': ')
                print(team['fullName'])
        print('Input your teams tricode, ex ORL, PHI, PHX etc:')
        team = input()
    return team


def set_presets(parser):
    '''
    set_presets(parser)
    Function used by config_settings to set presets of config.ini file
    '''
    fave_team = team_select()
    my_team = get_team_url(fave_team)
    parser.set('Favourite Team', 'team', str(my_team))
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
    with urllib.request.urlopen(url) as nba_url:
        data = json.loads(nba_url.read().decode())
        season = data['teamSitesOnly']['seasonYear']
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


def configure_app():
    '''
    Main config function to call all the configure settings needed to run the
    app
    '''
    config_settings()
    set_default_season()
    check_season()




if __name__ == '__main__':
    configure_app()
