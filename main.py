import json
import urllib.request
#import configapp

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


class MainApp(object):
    """A class representation of main app.
    """
    def __init__(self):
        self.CA = ConfigureApp() #call only when necesarry?
        self.config_display()

        self.SB = ScoreBoardUI()
        self.B = BoxScoreUI()
        self.S = ScheduleUI(next=True, last=True, full=False) #add to display
        self.TL = TeamLeadersUI()
        self.CS = StandingsUI(conference=True) #conference choice/add to display

    def run(self):
        self.display()

    def display(self):
        self.options()
        self.SB.display(horiz=True) #config option
        self.B.display()
        self.S.display()
        self.TL.display()
        self.CS.display()

    def config_display(self):
        if get_info(('Initial Config', 'config')) != 'True':
            print(f"Welcome to PyNBAScore\nPlease select your favourite team.")
            self.CA.configure()
            self.is_config = True

    def options(self):
        pass


if __name__ == '__main__':
    App = MainApp()
    App.run()
