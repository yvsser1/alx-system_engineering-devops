#!/usr/bin/python3
"""Function that prints hot posts for a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries RedditAPI and returns a list of hotpost titles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'AlxRedditApi/1.0 (by /u/yvsser1)'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list


if __name__ == '__main__':

    result = recurse('python')
    if result is not None:
        print(len(result))
    else:
        print("None")
