from functions import get_data

from nbaplayers import get_player_name
from nbateam import get_team_url

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_team, get_season

MAIN_FIVE_STATS = ['ppg', 'trpg', 'apg', 'bpg', 'spg']
main_five_stats = []

def get_team_leaders(team=None, season=None):
    """Gets raw json data for stat leaders for given team.

    Args:
        team: lowercase team name of team. ex: raptors, sixers, bulls
        season: Year of season start date. Ex: 2019 for the 2019/2020 season.

    Returns:
        Dict of raw json data from data.nba.net /leaders.json endpoint
    """
    if not team: team = get_team()
    if not date: date = get_season()

    url1 = 'http://data.nba.net/prod/v1/'
    url_end = '/leaders.json'
    url = str(url1) + str(date) + '/teams/' + str(team.lower()) + str(url_end)

    data = get_data(url)
    return data


class TeamLeaders(object):
    """A class to sort and hold data from NBA's /leaders.json endpoint

    Attributes:
    """
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
