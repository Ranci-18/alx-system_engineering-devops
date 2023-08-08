#!/usr/bin/python3
"""function module"""
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    header = {"User-Agent": "Mozilla/5.0 (X11;\
              Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}
    url = "https://www.reddit.com/dev/api/r/\
    {}/hot.json?limit=10&after={}".format(subreddit, after)

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        data = response.json()
        top_posts = data['data']['children']
        for post in top_posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
