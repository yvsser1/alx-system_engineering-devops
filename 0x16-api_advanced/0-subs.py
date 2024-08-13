#!/usr/bin/python3
""" function that returns number of subs for a given subreddit. """
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'AlxRedditApi/1.0 (by /u/yvsser1)'
    }
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is not found or any other error occurs, return 0
            return 0
    except Exception as e:
        # If any exception occurs during the process, return 0
        print(f"An error occurred: {e}")
        return 0
