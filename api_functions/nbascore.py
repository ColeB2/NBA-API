from functions import get_data

'''TDOO: REMOVE UI Elements, '''
def get_score(gameId, date='20200120'):
    '''
    Gets the score of a given game given the gameId and the date
    Used in conjunction with get_today_gameId or get_last_gameId to aquire said
    gameId, and date

    param  : get_score(gameId, date)
    gameId : numberical code for give game, ex '0021900640'
    date   : date in YYYYMMDD format for given game

    EXAMPLE USES:
    req import  : from nbaschedule import get_last_gameId, get_today_gameId
    scores = get_last_gameId()
    my_score = get_score(gameId=scores[0], date=scores[1])
    returns     : score as well as prints to console
    '''

    url_start = 'http://data.nba.net/prod/v1/'
    url = str(url_start) + str(date) + str('/scoreboard.json')

    data = get_data(url)
    x = data['games']

    score = None
    found = False
    for game in x:
        if gameId == game['gameId']:
            y = game
            score = (game['hTeam']['triCode'], game['hTeam']['score'],
                     game['vTeam']['triCode'], game['vTeam']['score'])
            found = True
    if found == False:
        print('Game not Found')

    return score

if __name__ == '__main__':
    print('Importing get_today_gameId, get_last_gameId')
    from nbaschedule import get_today_gameId, get_last_gameId

    print("Checking Raptors/Hawk game, gameId: '0021900640', date='20200120'")
    raptors_hawks = '0021900640'

    my_score = get_score(gameId=raptors_hawks, date='20200120')
    print(my_score)
    print()

    print('getting today game id from defaul favourite team')
    x = get_today_gameId()
    print(x)
    print('Score for today game')
    my_score = get_score(gameId=x[0], date=x[1])
    print(my_score)
    print()

    print('getting last game id')
    z = get_last_gameId('2019', 'raptors')
    print("Score for: '2019, 'raptors'")
    my_score = get_score(gameId=z[0], date=z[1])
    print(my_score)
    print()
