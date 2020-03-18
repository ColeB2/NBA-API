from ui_functions import Widget

import os, sys
sys.path.append(os.path.join('.', 'api_functions'))
from nbateamleaders import TeamLeaders
from nbaplayers import PlayerInfo
from functions import get_full_name

class TeamLeadersUI(Widget):
    """A class to represent an NBA team's team leaders.

    Attributes:
        TL: TeamLeaders object which holds all stats/methods for team leaders.
        PI: PlayerInfo object which holds all player information for ea player.
        headers: Representation of important headers to be used for printing.
        data_headers: Copy of TL.leader_keys list from TL object.
    """
    def __init__(self, team=None, season=None, player_info_obj=None):
        self.TL = TeamLeaders(team, season)
        if player_info_obj:
            self.PI = player_info_obj
        else:
            self.PI = PlayerInfo()
        self.headers = ['PTS/G', 'REB/G', 'AST/G', 'FG%',
            '3PT%', 'FT%', 'BLK/G','STL/G', 'TO/G',
            'PF/G']
        self.data_headers = self.TL.leader_keys.copy()


    def display(self, horiz=True):
        """Prints the team leaders of chosen team to the console.

        Args:
            horiz: Boolean, decides whether to print horizontal or not.
        """
        if horiz:
            self.horizontal_display(self.TL)


    """HORIZONTAL DISPLAY METHODS"""
    def create_nested_list(self, data):
        """Creates a list of lists to be passed on to the
        Parent Class, Widget's, create_tabulate_table method.

        Args:
            data: The data to be parsed through to create the lists.

        Returns:
            List of lists, headers, leaders.
            headers: list of stats and value of said stats.
            leaders: list of the players who lead said stats.
        """
        leaders = []
        headers = []

        NAMES = get_full_name()
        print(NAMES)
        for key, value in data.leaders.items():
            if key in self.data_headers:
                idx = int(self.data_headers.index(key))

                if type(value) is list: ##2+ stat leaders
                    header = f"{self.headers[idx]}: {value[0]['value']}"
                    leader = f""
                    for player in value:
                        first, last = self.PI.get_player_name(player['personId'])
                        if NAMES == 'False':
                            first = f"{first[0:1]}."
                        if player == value[-1]:
                            leader += f"{first} {last}"
                        else:
                            leader += f"{first} {last}/"
                else: #single stat leader
                    header = f"{self.headers[idx]}: {value['value']}"
                    first, last = self.PI.get_player_name(value['personId'])
                    if NAMES == 'False':
                        first = f"{first[0:1]}."
                    leader = f"{first} {last}"

                headers.append(header)
                leaders.append(leader)

        return [headers, leaders]

    def get_nested_list(self, data):
        """Calls create_nested_list method in order to get the values for the
        nested list to be passed on to create_tabulate_table method"""
        return self.create_nested_list(data)



if __name__ == '__main__':
    TL = TeamLeadersUI()
    TL.display()
