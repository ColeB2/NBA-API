import json
import urllib.request
#import configapp

import os, sys
sys.path.append(os.path.join('.', 'ui'))

from nba_boxscore_ui import BoxScoreUI
from nba_schedule_ui import ScheduleUI


if __name__ == '__main__':
    
    B = BoxScoreUI()
    B.display()

    S = ScheduleUI()
    S.display(True, True)
