def get_top_retweeted(tweets, amount):
    top_retweeted = sorted(
        tweets, key=lambda tweet: tweet["retweetCount"], reverse=True
    )[:amount]
    return top_retweeted


def get_top_users_by_tweets(tweets, amount):
    users = {}
    for tweet in tweets:
        username = tweet["user"]["username"]
        if username not in users:
            users[username] = 1
        else:
            users[username] += 1

    users_array = list(users.items())
    top_users = sorted(users_array, key=lambda user: user[1], reverse=True)[:amount]
    top_usernames = [user[0] for user in top_users]
    return top_usernames


def get_top_days_by_tweets(tweets, amount):
    days = {}
    for tweet in tweets:
        day = tweet["date"][:10]
        if day not in days:
            days[day] = 1
        else:
            days[day] += 1

    days_array = list(days.items())
    top_days = sorted(days_array, key=lambda day: day[1], reverse=True)[:amount]
    top_days = [day[0] for day in top_days]
    return top_days


def get_tweet_hashtags(tweet):
    body = tweet["content"]
    hashtags = [hashtag for hashtag in body.split() if hashtag.startswith("#")]
    return hashtags


def get_top_hastags(tweets, amount):
    hashtags = {}
    for tweet in tweets:
        hashtags_in_tweet = get_tweet_hashtags(tweet)
        for hashtag in hashtags_in_tweet:
            if hashtag not in hashtags:
                hashtags[hashtag] = 1
            else:
                hashtags[hashtag] += 1

    hashtags_array = list(hashtags.items())
    top_hashtags = sorted(hashtags_array, key=lambda hashtag: hashtag[1], reverse=True)[
        :amount
    ]
    top_hashtags = [hashtag[0] for hashtag in top_hashtags]
    return top_hashtags
