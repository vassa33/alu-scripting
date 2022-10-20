#!/usr/bin/python3

import requests
import json
subreddit = 'python'
limit = '10'
timeframe = 'month' # hour, day, week, month, year, all
listing = 'top' # controversial, best, hot, new, random, rising, top

def get_reddit(subreddit, listing, limit, timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        response = requests.get(base_url, headers= {'user-agent': 'yourbot'})
    except:
        print ('An error Occured')
    return response.json()

r = get_reddit(subreddit,listing,limit,timeframe)

def get_post_titles(r):

    '''
    get a list of the top 100 post titles
    '''

    posts = []

    for post in r['data']['children']:

        x = post ['data']['title']
        posts.append(x)

    return posts

def keys():
    for posts in r['data']['children']:
        for keys in posts['data'].keys():
            print(keys)

key_list = keys()
print(key_list) 


