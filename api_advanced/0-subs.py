#!/usr/bin/python3
"""
returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # https://stackoverflow.com/questions/10606133/
    # sending-user-agent-using-requests-library-in-python
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    req = requests.get(url, headers=headers).json()
    subs = req.get('data', {}).get('subscribers')
    if not subs:
        return 0
    return subs
