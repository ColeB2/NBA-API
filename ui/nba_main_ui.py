import json
import urllib.request
import colorama

import os, sys
sys.path.append(os.path.join('.', 'ui'))
sys.path.append(os.path.join('.', 'config'))
sys.path.append(os.path.join('.', 'api_functions'))

from configapp import ConfigureApp
from getconfiginfo import get_info

from nbateam import TeamInfo
from nbaplayers import PlayerInfo

from nba_boxscore_ui import BoxScoreUI
from nba_schedule_ui import ScheduleUI
from nba_teamleaders_ui import TeamLeadersUI
from nba_scores_ui import ScoreBoardUI
from nba_standings_ui import StandingsUI



class NBA_UI():
    def __init__(self):
        colorama.init()
        self.CA = ConfigureApp()
        self.TI = TeamInfo()
        self.PI = PlayerInfo()



    def create_widgets(self):
        self.SB = ScoreBoardUI()
        self.B = BoxScoreUI()
        self.S = ScheduleUI(next=True, last=True, full=False)
        #add to display
        self.TL = TeamLeadersUI(player_info_obj=self.PI)
        self.ST = StandingsUI(team_info_obj=self.TI)


    def run(self, scoreboard=True, boxscore=True, score=True,
            teamleaders=True, standings=True):
        #self.config_display()
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
        print(f"Welcome to PyNBAScore\n")
        self.CA = ConfigureApp()
        self.CA.configure()
        print(f"Loading Dashboard...")


    def quit(self):
        colorama.deinit()
        sys.exit()


    def options(self):
        while True:
            print(f"\nQ: Quit\n1: Standings\n2: Schedule\n"
                  f"3: Team Leaders\nC: Config Options\nD: Dashboard")
            user_input = input()
            if user_input == '1':
                self.standings_ui()
            elif user_input == '2':
                self.schedule_ui()
            elif user_input == '3':
                self.team_leaders_ui()
            elif user_input.lower() == 'c':
                self.config_dashboard_ui()
            elif user_input.lower() == 'd':
                self.dashboard()
            elif user_input.lower() == 'q':
                self.quit()


    """Widget UIS. Used to navigate stats."""
    def boxscore_ui(self):
        print(f"Select a boxscore to look at.")

    """Standings UI"""
    def standings_ui(self):
        print(f"Select an option\n1: Eastern Conference\n2: Western Conference"
            f"\n3: Division Standings \na: Both Conferences \n")
        user_input = input()
        if user_input == '1':
            self.ST.display(conference='east', division=None)
        elif user_input == '2':
            self.ST.display(conference='west', division=None)
        elif user_input == 'a':
            self.ST.display(conference='east', division=None)
            self.ST.display(conference='west', division=None)
        elif user_input == '3':
            print(f"Select a division:"
                f"\n1: Atlantic \n2: Central \n3: SouthEast \n4: Pacific"
                f"\n5: SouthWest \n6: NorthWest \na: All divisions" )
            user_input = input()
            if user_input == '1':
                self.ST.display(division='atlantic', conference='east')
            elif user_input == '2':
                self.ST.display(division='central', conference='east')
            elif user_input == '3':
                self.ST.display(division='southeast', conference='east')
            elif user_input == '4':
                self.ST.display(division='pacific', conference='west')
            elif user_input == '5':
                self.ST.display(division='southwest', conference='west')
            elif user_input == '6':
                self.ST.display(division='northwest', conference='west')
            elif user_input == 'a':
                self.ST.display(division='atlantic', conference='east')
                self.ST.display(division='central', conference='east')
                self.ST.display(division='southeast', conference='east')
                self.ST.display(division='pacific', conference='west')
                self.ST.display(division='southwest', conference='west')
                self.ST.display(division='northwest', conference='west')
        elif user_input == 'q':
            self.quit()

    def schedule_ui(self):
        """UI options for checking teams schedule.
        TODO:
        Adjust scheduleUI to have time start for full/vertical options
        Config options for user to select default showing for option.
        """
        print(f"Select team to check out their schedule.")
        for team in self.TI.teamsTRI:
            print(team)
        user_input = input("\nTricode: ")
        team = self.TI.get_team(user_input.upper(), id_option='tricode',
            id_return='nickname')

        print(f"Team Selected: {team}...Loading Data...")
        if not team:
            print(f"Invalid tricode: {user_input}, couldn't find team")
        else:
            TS = ScheduleUI(team=team.lower())
            TS.display(horiz=True)

    def team_leaders_ui(self):
        print(f"Select a team to check their leaders" )
        for team in self.TI.teamsTRI:
            print(team)
        user_input = input("\nTricode: ")
        team = self.TI.get_team(user_input.upper(), id_option='tricode',
            id_return='nickname')

        print(f"Team Selected: {team}...Loading Data...")
        if not team:
            print(f"Invalid tricode: {user_input}, couldn't find team")
        else:
            TL = TeamLeadersUI(team=team)
            TL.display()

    def config_dashboard_ui(self):
        print(f"Config Dashboard Not Implemented.")




if __name__ == '__main__':
    UI = NBA_UI()
    UI.run()
