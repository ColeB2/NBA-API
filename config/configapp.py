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
    def __init__(self, team_info_obj=None):
        self.config_folder = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(self.config_folder, 'config.ini')

        self.config = configparser.RawConfigParser()
        if self.config.read(self.config_path) == []:
            self.create_config()

        if team_info_obj:
            self.TI = team_info_obj
        else:
            self.TI = TeamInfo()


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
        self.config.set('Default', 'team', str(my_team))
        self.config.set('Initial Config', 'config', 'True')
        self.config.set('Default', 'season', self._set_default_season())
        self.config.set('Default', 'color', 'False')
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def create_config(self):
        self.config['Initial Config'] = {'config': 'False'}
        self.config['Default'] = {
                             'team': None,
                             'season': '2019',
                             'color': 'False',
                             'standing': 'conference'}
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)


    def _team_select(self):
        """Displays all NBA teams, and provides input to chose a team.

        TODO: break up code, separate options and functions to grab team.
        UI method.
        """
        teams = []
        for team in self.TI.teamsTRI:
            print(team)
            teams.append(team)

        while True:
            print(f"Please input desired teams tricode, ex ORL, PHI, PHX etc:")
            team = input()
            if team.upper() in teams:
                return str(team.upper())
            elif team.lower() == 'q':
                sys.exit()
            else:
                print(f"invalid input, try again.")


    def _set_default_season(self):
        """Sets season default to the year of current season, done so for when
        season is left blank in any function that reqeuires it
        """
        url = 'http://data.nba.net/10s/prod/v1/today.json'
        get_data(url)
        season = get_data(url)['teamSitesOnly']['seasonYear']

        return str(season)


    def check_season(self):
        """
        Checks to make sure the season setting is correct, then corrects it
        """
        current_season = self._set_default_season()
        season_check = self.config.get('Default', 'season')
        if season_check != current_season:
            self.config.set('Default', 'season', current_season)
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)

    """Change Config Menus"""
    def toggle_color(self):
        if self.config.get('Default', 'color') != 'True':
            print('Color off, turning on')
            self.config.set('Default', 'color', 'True')
        else:
            print('Color Turned On')
            self.config.set('Default', 'color', 'False')
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def toggle_standings(self):
        if self.config.get('Default', 'div_stand') == 'conference':
            self.config.set('Default', 'div_stand', 'division')
        else:
            self.config.set('Default', 'div_stand', 'conference')

        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def toggle_full_name(self):
        if self.config.get('Default', 'full_names_players') == 'True':
            self.config.set('Default', 'full_names_players', 'False')
        else:
            self.config.set('Default', 'full_names_players', 'True')
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)








if __name__ == '__main__':
    CA = ConfigureApp()
    CA.configure()
