import json
import urllib.request
#import configapp

import os, sys
sys.path.append(os.path.join('.', 'ui'))
print(sys.path)
from nba_boxscore_ui import BoxScoreUI
from api_functions import nbagameboxscore


if __name__ == '__main__':
    B = BoxScoreUI()
    B.display()
