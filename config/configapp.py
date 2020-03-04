"""
configapp.py - An object with methods used in configuring the main app to work
with the users favourite team
"""
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


class ConfigureApp(object):

    def __init__(self):
        self.config_folder = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(self.config_folder, 'config.ini')

        self.TI = TeamInfo()
        self.config = configparser.RawConfigParser()
        self.config.read(self.config_path)

    def configure(self):
        self.config_settings()
        self._set_default_season()
        self.check_season()

    def config_settings(self):
        if self.config.get('Initial Config', 'config') != 'True':
            self.set_presets()


    def set_presets(self):
        """Sets initial presets in config .ini file for app to run properly.
        Includes:
            season year, team of choice...
        """
        fave_team = self._team_select()
        my_team = self.TI.get_team(fave_team.upper(), id_return='urlName')
        self.config.set('Team', 'team', str(my_team))
        self.config.set('Initial Config', 'config', 'True')
        self.config.set('Values', 'season', self._set_default_season())
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def _team_select(self):
        """Displays all NBA teams, and provides input to chose a team.

        TODO: break up code, separate options and functions to grab team.
        UI method.
        """
        teams = []
        for team in self.TI.standard:
            if team['isNBAFranchise'] == True:
                teams.append(team['tricode'])
                print(f"{team['tricode']}: {team['fullName']}")

        while True:
            print(f"Input your teams tricode, ex ORL, PHI, PHX etc:")
            team = input()
            if team.upper() in teams:
                return str(team.upper())
            else:
                print(f"invalid input, try again.")


    def _set_default_season(self):
        '''Sets season default to the year of current season, done so for when
        season is left blank in any function that reqeuires it

        TODO:
        use get_data funcs, '''
        url = 'http://data.nba.net/10s/prod/v1/today.json'
        get_data(url)
        season = get_data(url)['teamSitesOnly']['seasonYear']

        return str(season)


    def set_default_date(self):
        '''Sets date default date to proper format, done for functions that
        require a date in the url, and one isn't given'''
        pass


    def check_season(self):
        """
        Checks to make sure the season setting is correct, then corrects it
        """
        current_season = self._set_default_season()
        season_check = self.config.get('Values', 'season')
        if season_check != current_season:
            self.config.set('Values', 'season', current_season)
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)




if __name__ == '__main__':
    CA = ConfigureApp()
    CA.configure()
