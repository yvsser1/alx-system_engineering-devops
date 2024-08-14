#!/usr/bin/python3
"""Function that counts the words in all hotposts for a given subreddit."""
from collections import Counter
import requests
import re


def count_words(subreddit, word_list, after=None, word_counts=None):
    if word_counts is None:
        word_counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'AlxRedditApi/1.0 (by /u/yvsser1'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return

    posts = data.get('data', {}).get('children', [])
    if not posts:
        print_results(word_counts, word_list)
        return

    for post in posts:
        title = post['data']['title'].lower()
        words = re.findall(r'\b[\w\']+\b', title)
        for word in words:
            if word.lower() in (w.lower() for w in word_list):
                word_counts[word.lower()] += 1

    after = data['data'].get('after')
    count_words(subreddit, word_list, after, word_counts)  # Always recurse

    if not after:  # Only print results in the base case
        print_results(word_counts, word_list)


def print_results(word_counts, word_list):
    sorted_counts = sorted(
        ((word, count) for word in word_list
         for count in [word_counts[word.lower()]] if count > 0),
        key=lambda x: (-x[1], x[0].lower())
    )
    for word, count in sorted_counts:
        print(f"{word.lower()}: {count}")
