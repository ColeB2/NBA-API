import json
import urllib.request
import datetime


def get_data(url):
    """
    Gets the json data from given url and returns said data

    Args:
        url: URL of endpoint we want to retrieve data from

    Returns:
        Full dumn of json data from the given url
    """
    with urllib.request.urlopen(url) as nba_url:
        data = json.loads(nba_url.read().decode())

    return data

def get_today_date():
    """Gets todays date and formats it for api function use."""
    return ''.join(str(datetime.date.today()).split('-'))

def get_season_year():
    pass


if __name__ == '__main__':
    print(get_today_date())
