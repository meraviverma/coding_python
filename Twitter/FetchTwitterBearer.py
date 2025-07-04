# Import libraries
import tweepy
import pandas as pd

# Function to print tweet metadata
def print_tweet_data(n, tweet_data):
    print(f"\nTweet {n}:")
    print(f"ID: {tweet_data[0]}")
    print(f"Text: {tweet_data[1]}")
    print(f"Username: {tweet_data[2]}")
    print(f"Created At: {tweet_data[3]}")
    print(f"Hashtags: {tweet_data[4]}")

# Function to scrape tweets using Twitter API v2
def scrape_tweets_v2(query, max_tweets):
    # Initialize DataFrame
    db = pd.DataFrame(columns=['id', 'text', 'username', 'created_at', 'hashtags'])

    # Initialize Tweepy Client
    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

    # Fetch tweets with metadata
    response = client.search_recent_tweets(
        query=query,
        max_results=max_tweets,
        expansions=['author_id'],
        tweet_fields=['id', 'text', 'created_at', 'entities'],
        user_fields=['username']
    )

    user_map = {}
    if response.includes and 'users' in response.includes:
        for user in response.includes['users']:
            user_map[user.id] = user.username

    # Parse tweets
    for i, tweet in enumerate(response.data, start=1):
        hashtags = []
        if tweet.entities and 'hashtags' in tweet.entities:
            hashtags = [tag['tag'] for tag in tweet.entities['hashtags']]

        username = user_map.get(tweet.author_id, "N/A")
        tweet_data = [tweet.id, tweet.text, username, tweet.created_at, hashtags]
        db.loc[len(db)] = tweet_data
        print_tweet_data(i, tweet_data)

    db.to_csv("scraped_v2_tweets.csv", index=False, encoding="utf-8-sig")
    print("\n✅ Scraping completed and saved to 'scraped_v2_tweets.csv'.")

# Main script
if __name__ == '__main__':
    # 🔐 Paste your Bearer Token below (Twitter API v2)
    BEARER_TOKEN = "XXXXXXX"

    print("🔍 Enter Twitter hashtag or search query (e.g. #AI):")
    query = input().strip()

    print("📦 Enter number of tweets to fetch (max 100 per request):")
    num_tweets = int(input())

    scrape_tweets_v2(query=query, max_tweets=num_tweets)