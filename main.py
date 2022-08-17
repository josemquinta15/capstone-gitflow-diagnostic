import json

from utils import (
    get_top_retweeted,
    get_top_users_by_tweets,
    get_top_days_by_tweets,
    get_top_hastags,
)


def get_tweets(filename):
    with open(filename, "r") as file:
        tweets = [json.loads(line) for line in file.readlines()]
        return tweets


def main():
    tweets = get_tweets("test_tweets.json")
    print(get_top_retweeted(tweets, 10))
    print(get_top_users_by_tweets(tweets, 10))
    print(get_top_days_by_tweets(tweets, 10))
    print(get_top_hastags(tweets, 10))


if __name__ == "__main__":
    main()
