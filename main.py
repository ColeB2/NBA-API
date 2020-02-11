import json
import urllib.request
#import configapp

import os, sys
sys.path.append(os.path.join('.', 'ui'))

from nba_boxscore_ui import BoxScoreUI
from nba_schedule_ui import ScheduleUI
from nba_teamleaders_ui import TeamLeadersUI
from nba_scores_ui import ScoreBoardUI


if __name__ == '__main__':
    TL = TeamLeadersUI()
    TL.display()

    SB = ScoreBoardUI()
    SB.display()

    B = BoxScoreUI()
    B.display()

    S = ScheduleUI(next=True, last=True, full=False)
    S.display()
