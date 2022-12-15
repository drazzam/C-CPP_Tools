import tweepy
from textblob import TextBlob

# Enter your Twitter API keys here
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets containing keywords related to the fields of interest
tweets = tweepy.Cursor(api.search,
                       q="Interventional Neuroradiology OR Endovascular Neurosurgery OR Interventional Neurology OR Neurointervention OR Neuroendovascular OR Endovascular Surgical Neuroradiology OR Neurointerventional Surgery",
                       lang="en").items(1000)

# Keep track of the trends and most interactive accounts
trends = {}
accounts = {}

# Process each tweet
for tweet in tweets:
    # Parse the tweet text
    tweet_text = tweet.text
    tweet_text = tweet_text.lower()
    tweet_text = tweet_text.replace(".", "")
    tweet_text = tweet_text.replace(",", "")

    # Count the number of times each keyword appears in the tweet text
    for keyword in ["Interventional Neuroradiology", "Endovascular Neurosurgery", "Interventional Neurology", "Neurointervention", "Neuroendovascular", "Endovascular Surgical Neuroradiology", "Neurointerventional Surgery"]:
        if keyword in tweet_text:
            if keyword in trends:
                trends[keyword] += 1
            else:
                trends[keyword] = 1

    # Count the number of times each user is mentioned in the tweet text
    tweet_blob = TextBlob(tweet_text)
    mentions = tweet_blob.mentions
    for mention in mentions:
        if mention in accounts:
            accounts[mention] += 1
        else:
            accounts[mention] = 1

# Print the trends
print("Trends:")
for trend, count in trends.items():
    print(f"{trend}: {count}")

# Print the most interactive accounts
print("\nMost interactive accounts:")
for account, count in accounts.items():
    print(f"{account}: {count}")
