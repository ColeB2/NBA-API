'''
nbateam.py - Acquires NBA team code given either:
city: Atlanta
fullName: Chicago Bulls
tricode: DAL
nickname: Mavericks
teamid: 1610612744
'''
from functions import get_data

import sys, os
sys.path.append(os.path.abspath(os.path.join('.', 'config')))
from getconfiginfo import get_season



def get_team_url(identifier):
    '''
    Gets the teamUrl name via some sort of identifier

    param      : get_team_url(identifier)
    identifiers: City, Full Team Name, tri code, nickname, teamId
    city       : Atlanta
    fullName   : Chicago Bulls
    tricode    : DAL
    nickname   : 76ers
    teamId     : 1610612744
    example    : get_team_url('ToRoNtO')

    returns    : urlName which is used in various urls to find teams games,
    stats, schedules etc. ex: raptors, hawks, sixers
    example    : 'raptors'
    '''
    season_year = get_season()
    url = 'http://data.nba.net/prod/v2/' + str(season_year) + '/teams.json'

    data = get_data(url)
    x = data['league']
    y = x['standard']

    team_url = str()
    for team_dict in y:
        #print(team_dict)
        for value in team_dict:
            team_id = team_dict[value]
            try:
                if team_id.lower() == str(identifier).lower():
                    team_url = team_dict['urlName']
            except AttributeError:
                pass



    return team_url if team_url else 'Invalid Identifier'



if __name__ == '__main__':
    print(get_team_url('Raptors'))
    print(get_team_url('ToRoNtO RaPtOrS'))
    print(get_team_url('ChicaGo Bulls'))
    print(get_team_url('DAL'))
    print(get_team_url('ToRoNtO'))
    print(get_team_url('HAWKS'))
    print(get_team_url('ATLANTA'))
    print(get_team_url('Magic'))
    print(get_team_url('FAIL'))
