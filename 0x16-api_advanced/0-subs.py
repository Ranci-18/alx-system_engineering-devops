#!/usr/bin/python3
import json
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/dev/api/r/{:s}/about".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        data = response.json()
        subscribers = int(data['data']['subscribers'])
        return subscribers
    else:
        return 0
