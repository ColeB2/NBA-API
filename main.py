import json
import urllib.request
#import configapp

import os, sys
sys.path.append(os.path.join('.', 'ui'))
sys.path.append(os.path.join('.', 'config'))

from configapp import configure_app
from getconfiginfo import get_info

from nba_boxscore_ui import BoxScoreUI
from nba_schedule_ui import ScheduleUI
from nba_teamleaders_ui import TeamLeadersUI
from nba_scores_ui import ScoreBoardUI
from nba_standings_ui import StandingsUI


class Main(object):
    """A class representation of main app.
    """
    def __init__(self):
        self.config = self.get_info()
        pass

    def display(self):
        pass

    def config_display(self):
        pass


if __name__ == '__main__':
    SB = ScoreBoardUI()
    SB.display(horiz=True)

    B = BoxScoreUI()
    B.display()

    S = ScheduleUI(next=True, last=True, full=False)
    S.display()

    TL = TeamLeadersUI()
    TL.display()

    CS = StandingsUI(conference=True)
    CS.display()
