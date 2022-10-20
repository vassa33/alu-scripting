#!/usr/bin/python3
"""
Module doc
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Doc"""
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    if requests.get(url, headers=headers, allow_redirects=False):
        if after is None:
            return hot_list
        req = requests.get(url, headers=headers, allow_redirects=False).json()
        items = req.get('data', {}).get('children', [])
        for item in items:
            hot_list.append(item.get('data').get('title'))
        after = req.get('data').get('after')
        return recurse(subreddit, hot_list, after)
    else:
        return None
