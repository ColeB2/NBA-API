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

def get_date_before(date=None):
    """Gets the date before given date"""
    if not date: date = get_today_date()
    date_time_obj = datetime.datetime.strptime(date, '%Y%m%d')
    date = str(date_time_obj - datetime.timedelta(days=1))[:10]
    return ''.join(str(date).split('-'))

def get_season_year():
    pass


if __name__ == '__main__':
    print(get_today_date())
    print('yesterday: ' + str(get_date_before()))

    print('get_date_before: ' + str(get_date_before('20200101')))
