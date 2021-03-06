from functions import get_data, get_season_year, get_team



def get_team_data(season=None):
    """Gets raw json data for all teams.

    Args:
        season: Year of season start date. Ex: 2019 for the 2019/2020 season.

    Returns:
        Dict of raw json data from data.nba.net.../teams.json endpoint
    """
    if not season: season = get_season_year()
    url = 'http://data.nba.net/prod/v2/' + str(season) + '/teams.json'

    data = get_data(url)
    return data

class TeamInfo(object):
    """A class to sort and hold data from NBA's /team.json endpoint

    Attributes:


    """
    def __init__(self, season=None):
        self.raw_data = get_team_data(season)
        self._internal = self.raw_data['_internal']
        self.league = self.raw_data['league']
        self.standard = self.league['standard']

        self.identifiers = ['city', 'altCityName', 'fullName', 'tricode',
            'teamId', 'nickname', 'urlName', 'teamShortName']

        self.teamsTRI = self.create_nba_list()


    def get_conf_division(self, team=None, id_option=None):
        if team == None:
            team = get_team()
            for teams in self.standard:
                if teams['urlName'] == team.lower():
                    return (teams['confName'], teams['divName'])

        elif team != None and id_option == None:
            team = self.get_team(team)
            for teams in self.standard:
                if teams['urlName'] == team['urlName'].lower():
                    return (teams['confName'], teams['divName'])

        elif team != None and id_option != None:
            team = self.get_team(team, id_option=id_option, id_return=None)

        print('Could not find division')

    def get_team(self, identifier, id_option=None, id_return=None):
        """Gets identiy of a team, given an identifier, and id option.
        If ID option is blank, will got through full list of identifiers.

        Args:
            identifier: str, id of team, ex, name, tricode, teamId etc.
            id_option: option to look up id of team, example, search by city,
                fullName, tricode. Used to shorten the amount of searching.
            id_return: option to return specific part of id, if None, return
                full team dictionary.

        Returns:
            Returns list of identifying options for team.
        """
        for team in self.standard:
            if team['isNBAFranchise'] == True:
                for ID in self.identifiers:
                    if team[ID].lower() == identifier.lower():
                        if id_return:
                            return team[str(id_return)]
                        else:
                            return team

    def create_nba_list(self):
        teams = []
        for team in self.standard:
            if team['isNBAFranchise']:
                teams.append(team['tricode'])
        return teams



if __name__ == '__main__':
    TI = TeamInfo()
    print(f"{TI.raw_data.keys()}")
    print(f"{TI._internal.keys()}")
    print(f"{TI.league.keys()}")
    print(f"{TI.standard}")
    print(f"{TI.standard[0].keys()}")

    print('GET CONF_DIVISION')
    print(f"{TI.get_conf_division('raptors')}")
    print(f"{TI.get_conf_division()}")


    print('GET TEAM')
    print(TI.get_team('1610612761', id_return='urlName'))
    print(TI.get_team('raptors'))
    print(TI.get_team('1610612761', 'teamId', 'nickname'))

    for team in TI.standard:
        if team['isNBAFranchise'] == True:
            print(team)
