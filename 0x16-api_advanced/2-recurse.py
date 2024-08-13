#!/usr/bin/python3
"""Function that prints hot posts for a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'AlxRedditApi/1.0 (by /u/yvsser1)'
    }
    params = {'limit': 100}
    if after:
        params['after'] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            if not posts:
                return hot_list
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code == 404:
            return None
        else:
            print(f"An error occurred: Status code {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
