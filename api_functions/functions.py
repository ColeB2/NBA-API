import json
import urllib.request
import datetime

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
sys.path.append(os.path.abspath(os.path.join('..', 'config')))
from getconfiginfo import get_info, quick_config_reset, ConfigError


def get_data(url):
    """
    Gets the json data from given url and returns said data

    Args:
        url: URL of endpoint we want to retrieve data from

    Returns:
        Full dump of json data from the given url
    """
    with urllib.request.urlopen(url) as nba_url:
        data = json.loads(nba_url.read().decode())

    return data

def get_today_date():
    """Gets todays date and formats it as a string for api function use in the
        YYYYMMDD format."""
    return ''.join(str(datetime.date.today()).split('-'))

def get_date_before(date=None):
    """Gets the date 1 day before given date and formats it as a string in the
        YYYYMMDD format"""
    if not date: date = get_today_date()
    date_time_obj = datetime.datetime.strptime(date, '%Y%m%d')
    date = str(date_time_obj - datetime.timedelta(days=1))[:10]
    return ''.join(str(date).split('-'))

def get_season_year():
    try:
        season = get_info(('Default', 'season'))
    except:
        data = get_data("https://data.nba.net/10s/prod/v1/today.json")
        season = data['teamSitesOnly']['seasonYear']
    return season

def get_team():
    try:
        team = get_info(('Default', 'team'))
        if team == 'None':
            raise ConfigError
    except:
        print(f"Reseting config info, re open app")
        quick_config_reset()
    return team

def handle_team_url_name(team):
    if ' ' in str(team):
        team = team.split(' ')[1]
        return team
    elif team == '76ers':
        return 'sixers'
    else:
        return str(team)

def get_color():
    color = get_info(('Default', 'color'))
    return color

def get_full_name():
    name = get_info(('Default', 'full_names_players'))
    return name


if __name__ == '__main__':
    print(get_today_date())
    print('yesterday: ' + str(get_date_before()))

    print('get_date_before: ' + str(get_date_before('20200101')))
