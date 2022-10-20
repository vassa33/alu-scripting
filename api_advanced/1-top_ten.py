#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        queries the Reddit API and prints the titles
        of the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    req = requests.get(url, headers=headers).json()
    top_post = req.get('data', {}).get('children', [])
    if not top_post:
        print('None')
    for post in top_post:
        print(post.get('data').get('title'))
