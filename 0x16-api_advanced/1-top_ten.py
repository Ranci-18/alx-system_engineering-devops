#!/usr/bin/python3
"""function module"""
import json
import requests


def top_ten(subreddit):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0)\
    Gecko/20100101 Firefox/115.0"}
    url = "https://www.reddit.com/dev/api/\
    r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        data = response.json()
        top_posts = data['data']['children']
        return top_posts
    else:
        return None
