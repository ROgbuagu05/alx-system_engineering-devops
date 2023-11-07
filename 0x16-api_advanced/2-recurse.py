#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests

def recurse(subreddit, hot_list=[]):
    """Returns None if subreddit is not found."""
    url = f"https://api.reddit.com/r/{subreddit}/hot?limit=100"
    response = requests.get(url, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()

    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    if data["data"]["after"]:
        return recurse(subreddit, hot_list)

    return hot_list
