import json
import urllib.request
import datetime


def get_data(url):
    """
    Gets the json data from given url and returns said data

    Args:
        url: URL of endpoint we want to retrieve data from

    Returns:
        Full dump of json data from the given url
    """
    with urllib.request.urlopen(url) as nba_url:
        data = json.loads(nba_url.read().decode())

    return data

def get_today_date():
    """Gets todays date and formats it for api function use."""
    return ''.join(str(datetime.date.today()).split('-'))

def get_yesterday_date():
    """Gets yesterdays date and formats it for api function use."""
    date = str(datetime.datetime.now() - datetime.timedelta(days=1))[:10]
    return ''.join(str(date).split('-'))

def get_season_year():
    pass


if __name__ == '__main__':
    print(get_today_date())
    print(get_yesterday_date())
