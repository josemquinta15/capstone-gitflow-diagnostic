def get_top_retweeted(tweets, amount):
    top_retweeted = sorted(
        tweets, key=lambda tweet: tweet["retweetCount"], reverse=True
    )[:amount]
    return top_retweeted
