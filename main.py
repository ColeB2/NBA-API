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
    S = ScheduleUI(next=True, last=True, full=False)
    S.display()

    SB = ScoreBoardUI()
    SB.display(horiz=True)

    B = BoxScoreUI()
    B.display()

    TL = TeamLeadersUI()
    TL.display()
