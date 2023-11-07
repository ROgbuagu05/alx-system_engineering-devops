#!/usr/bin/python3
"""
Function to query the Reddit API and print the titles
of the first 10 hot posts for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
            "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
