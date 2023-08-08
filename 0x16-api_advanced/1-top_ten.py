#!/usr/bin/python3
"""function module"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles of first 10
    hot posts listed for a given subreddit"""
    header = {"User-Agent": "Mozilla/5.0 (X11;\
              Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}
    url = "https://www.reddit.com/dev/api/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        data = response.json()
        top_posts = data['data']['children']
        for post in top_posts[:10]:
            print(post['data']['title'])
    else:
        print("None")
