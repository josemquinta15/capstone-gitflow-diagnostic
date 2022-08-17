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
