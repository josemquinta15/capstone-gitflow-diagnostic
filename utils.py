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
