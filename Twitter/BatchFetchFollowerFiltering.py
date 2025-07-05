"""
Fetch twitter data with the limit on Filtering of data

When Twitter says you’ve hit a rate limit, it’s not referring to how many tweets you've received… it’s counting how many requests you've made to the API.

"""
import tweepy
import pandas as pd
import yaml

# === Define script to read YAML ===

# Load bearer token from YAML
def load_bearer_token(app_name: str, yaml_path) -> str:
    with open(yaml_path, 'r') as file:
        config = yaml.safe_load(file)
        for app in config['TwitterApps']:
            if app['AppName'] == app_name:
                return app['BearerToken']
    raise ValueError(f"No bearer token found for AppName '{app_name}'")

def gettweet():
    # === 1. Set up your Bearer Token ===
    BEARER_TOKEN = load_bearer_token("hashtaganalysis030","D:\\StorageAccount\Config\\twitter\\twitter_config.yml")

    # === 2. Define your query & config ===
    QUERY = "#btst lang:en"  # Example: hashtag + filters
    MAX_TWEETS = 10  # Twitter free tier allows max 100 per request

    target_day = "2025-07-05"
    start_time = f"{target_day}T00:00:00Z"
    end_time = f"{target_day}T23:59:59Z"

    # === 3. Initialize Tweepy Client ===
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        wait_on_rate_limit=True
    )

    # === 4. Perform Tweet Search ===
    response = client.search_recent_tweets(
        query=QUERY,
        max_results=MAX_TWEETS,
        expansions=['author_id'],
        tweet_fields=['id', 'text', 'created_at', 'entities','referenced_tweets'],
        user_fields=['username', 'public_metrics']
    )

    # === 5. Map user IDs to follower count and usernames ===
    user_map = {}
    if response.includes and 'users' in response.includes:
        for user in response.includes['users']:
            user_map[user.id] = {
                'username': user.username,
                'followers_count': user.public_metrics['followers_count']
            }

    # === 6. Parse and filter tweets by follower count ===
    filtered_tweets = []
    for tweet in response.data:
        author = user_map.get(tweet.author_id)
        if author and author['followers_count'] > 10000:
            hashtags = [tag['tag'] for tag in tweet.entities.get('hashtags', [])] if tweet.entities else []
            filtered_tweets.append([
                tweet.id,
                tweet.text,
                author['username'],
                author['followers_count'],
                tweet.created_at,
                hashtags
            ])
            print(f"🧠 @{author['username']} ({author['followers_count']} followers): {tweet.text}")

    # === 7. Save to CSV ===
    df = pd.DataFrame(filtered_tweets, columns=[
        'tweet_id', 'text', 'username', 'followers_count', 'created_at', 'hashtags'
    ])
    df.to_csv("filtered_tweets.csv", index=False, encoding="utf-8-sig")
    print("\n✅ Saved filtered tweets to 'filtered_tweets.csv'.")

if __name__=="__main__":
    gettweet()

