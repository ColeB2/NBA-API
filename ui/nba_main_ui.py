import json
import urllib.request

import os, sys
sys.path.append(os.path.join('.', 'ui'))
sys.path.append(os.path.join('.', 'config'))

from configapp import ConfigureApp
from getconfiginfo import get_info

from nba_boxscore_ui import BoxScoreUI
from nba_schedule_ui import ScheduleUI
from nba_teamleaders_ui import TeamLeadersUI
from nba_scores_ui import ScoreBoardUI
from nba_standings_ui import StandingsUI

class NBA_UI():
    def __init__(self):
        pass
        #self.CA = ConfigureApp() #call only when necesarry?



    def create_widgets(self):
        self.SB = ScoreBoardUI()
        self.B = BoxScoreUI()
        self.S = ScheduleUI(next=True, last=True, full=False) #add to display
        self.TL = TeamLeadersUI()
        self.ST = StandingsUI(div_stand=False) #conference choice/add to display


    def run(self, scoreboard=True, boxscore=True, score=True,
            teamleaders=True, standings=True):
        self.create_widgets()
        self.dashboard(scoreboard, boxscore, score, teamleaders, standings)


    def dashboard(self, scoreboard=True, boxscore=True, score=True,
                teamleaders=True, standings=True):

        if scoreboard: self.SB.display(horiz=True) #config option
        if boxscore: self.B.display()
        if score: self.S.display()
        if teamleaders: self.TL.display()
        if standings: self.ST.display()
        self.options()


    def config_display(self):
        print(f"Welcome to PyNBAScore\nPlease select your favourite team.")
        self.CA = ConfigureApp()
        self.CA.configure()


    def options(self):
        print(f"Q: Quit\n1: Standings\n2: Schedule\n"
              f"3: BoxScore\n4: Team Leaders")
        User_input = input()
        if User_input == '1':
            print('standings')
            self.standings_ui()
        elif User_input == '2':
            self.schedule_ui()
        elif User_input == '3':
            self.boxscore_ui()
        elif User_input == '4':
            self.team_leaders_ui()
        elif User_input == 'Q':
            sys.exit()


    """Widget UIS. Used to navigate stats."""

    def boxscore_ui(self):
        pass

    """Standings UI"""
    def standings_ui(self):
        print(f"Select an option\n1: Eastern Conference\n2: Western Conference\n3: Division Standings \nMore")
        user_input = input()
        if user_input == '1':
            X = StandingsUI(conference=True, _team="kings")
            X.display()

    def schedule_ui(self):
        pass

    def team_leaders_ui(self):
        pass


if __name__ == '__main__':
    UI = NBA_UI()
    UI.run()
