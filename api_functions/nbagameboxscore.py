from functions import get_data
from nbaschedule import get_last_gameId

def get_boxscore_data(date=None, gameId=None):
    """Gets raw json data for given game.

    Args:
        date: The date of the given game using YYYYMMDD format.
        gameId: The gameId for given game. Acquired using a get_gameId fucntion.
    Returns:
        Dictionary of raw json data from the data.nba.net
    """
    if not date or not gameId:
        x = get_last_gameId()
        gameId, date = get_last_gameId()

    url_start = 'http://data.nba.net/prod/v1/'
    url = str(url_start) + str(date) + '/' + str(gameId) + '_boxscore.json'

    data = get_data(url)
    return data


if __name__ == '__main__':
    raw_data = get_boxscore_data()
    print('-----RAW DATA BREAKDOWN, DICT KEYS---------------------------------')
    print(raw_data.keys())
    print('\n-----_internal---------------------------------------------------')
    _internal = raw_data['_internal']
    print(_internal.keys())

    print('\n-----basicGameData-----------------------------------------------')
    basicGameData = raw_data['basicGameData']
    print(basicGameData.keys())
    print(basicGameData['arena'])
    print(basicGameData['hTeam'])
    print(basicGameData['vTeam'])

    print('\n-----previousMatchup---------------------------------------------')
    previousMatchup = raw_data['previousMatchup']
    print(previousMatchup.keys())

    print('\n-----STATS-------------------------------------------------------')
    stats = raw_data['stats']
    print(stats.keys())
    print('\n-----STATS BREAKDOWN---------------------------------------------')
    print('timesTied: ' + stats['timesTied'])
    print('leadChanges:' + stats['leadChanges'])
    print('vTeam: ' + str(stats['vTeam'].keys()))
    print('vTeam Totals :'  + str(stats['vTeam']['totals']))
    print('hTeam: ' + str(stats['hTeam'].keys()))
    print('hTeam Totals :'  + str(stats['hTeam']['totals']))
    print('activePlayers :' + str(stats['activePlayers'][0].keys()))
    print('activePlayers :' + str(stats['activePlayers']))

    print('\n-----TEST--------------------------------------------------------')
    print(str(stats['vTeam']['totals'].keys()))
    print('dict_keys(', end='')
    headers = ['NO', 'Name', 'MIN', 'FG', '3PT', 'FT','OR',
      'DR', 'TR', 'AST', 'STL', 'BLK', 'TOV', 'PF',  '+/-', 'PTS']
    print(headers)
