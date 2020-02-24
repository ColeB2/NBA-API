import json
import urllib.request
#import configapp

import os, sys
sys.path.append(os.path.join('.', 'ui'))

from nba_boxscore_ui import BoxScoreUI
from nba_schedule_ui import ScheduleUI
from nba_teamleaders_ui import TeamLeadersUI
from nba_scores_ui import ScoreBoardUI
from nba_standings_ui import StandingsUI


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
