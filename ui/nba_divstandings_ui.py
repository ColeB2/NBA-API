from ui_functions import Widget

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbadivstandings import DivStandings
from nbateam import TeamInfo

class DivStandingsUI(Widget):
    """A class to represent nba divisional standings

    Attributes:

    """
    def __init__(self, division=None):
        self.DS = DivStandings(division=division)
        self.TI = TeamInfo()


    def display(self, horiz=True):
        pass

    def create_nested_list(self, data):
        nested_list = []

    def get_nested_list(self, data):
        """Calls create_nested_list method in order to get the values for the
        nested list to be passed on to create_tabulate_table method"""
        return self.create_nested_list(data)



if __name__ == '__main__':
    DS = DivStandingsUI()
    DS.display()
