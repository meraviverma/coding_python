# Import modules
import pandas as pd
import tweepy

# Function to display tweet metadata
def print_tweet_data(n, tweet_info):
    print(f"\nTweet {n}:")
    print(f"Username: {tweet_info[0]}")
    print(f"Description: {tweet_info[1]}")
    print(f"Location: {tweet_info[2]}")
    print(f"Following Count: {tweet_info[3]}")
    print(f"Follower Count: {tweet_info[4]}")
    print(f"Total Tweets: {tweet_info[5]}")
    print(f"Retweet Count: {tweet_info[6]}")
    print(f"Tweet Text: {tweet_info[7]}")
    print(f"Hashtags Used: {tweet_info[8]}")

# Function to perform data extraction
def scrape_tweets(query: str, start_date: str, max_tweets: int):
    # Set up DataFrame
    tweet_db = pd.DataFrame(columns=[
        'username', 'description', 'location', 'following',
        'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags'
    ])

    # Search for tweets using Tweepy Cursor
    tweets = tweepy.Cursor(api.search_tweets,
                           q=query,
                           lang="en",
                           since_id=start_date,
                           tweet_mode='extended').items(max_tweets)

    for i, tweet in enumerate(tweets, start=1):
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = [ht['text'] for ht in tweet.entities['hashtags']]

        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text

        tweet_info = [username, description, location, following,
                      followers, totaltweets, retweetcount, text, hashtags]

        tweet_db.loc[len(tweet_db)] = tweet_info
        print_tweet_data(i, tweet_info)

    # Save to CSV
    tweet_db.to_csv("scraped_tweets.csv", index=False, encoding="utf-8-sig")
    print("\n✅ Scraping completed and saved to 'scraped_tweets.csv'.")

# Main Execution
if __name__ == '__main__':
    # Twitter API credentials (from your developer account)
    consumer_key = "XXXXX"
    consumer_secret = "XXXXX"
    access_key = "XXXXX"
    access_secret = "XXXXX"

    # Authenticate and initialize Tweepy API with rate-limit handling
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Inputs
    query = input("🔍 Enter Twitter hashtag or search query:\n")
    start_date = input("📅 Enter date since tweets are required (yyyy-mm-dd):\n")
    max_tweets = 100

    scrape_tweets(query, start_date, max_tweets)