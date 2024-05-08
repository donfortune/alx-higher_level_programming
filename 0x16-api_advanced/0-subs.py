#!/usr/bin/python3
""" A script that queries the Reddit API and returns the number of subscribers
"""
import requests
import json


def number_of_subscribers(subreddit_name):
    if  not subreddit_name:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit_name)
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
    
    