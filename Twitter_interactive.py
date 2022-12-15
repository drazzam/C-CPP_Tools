import tweepy

# Replace these with your own Twitter API keys
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch the most recent 200 tweets from your timeline
tweets = api.home_timeline(count=200)

# Track the users who have interacted with your tweets
interactive_users = {}

# Loop through your tweets and track the likes, retweets, and comments on each one
for tweet in tweets:
  # Get the users who have liked the tweet
  likes = api.favorites(tweet.id)

  # Loop through the users who have liked the tweet and add them to the dictionary
  for user in likes:
    if user.id not in interactive_users:
      interactive_users[user.id] = {"likes": 1}
    else:
      interactive_users[user.id]["likes"] += 1

  # Get the users who have retweeted the tweet
  retweets = api.retweets(tweet.id)

  # Loop through the users who have retweeted the tweet and add them to the dictionary
  for user in retweets:
    if user.id not in interactive_users:
      interactive_users[user.id] = {"retweets": 1}
    else:
      interactive_users[user.id]["retweets"] += 1

  # Get the users who have commented on the tweet
  comments = api.comments(tweet.id)

  # Loop through the users who have commented on the tweet and add them to the dictionary
  for user in comments:
    if user.id not in interactive_users:
      interactive_users[user.id] = {"comments": 1}
    else:
      interactive_users[user.id]["comments"] += 1

# Sort the dictionary of interactive users by the total number of interactions
sorted_users = sorted(interactive_users.items(), key=lambda x: sum(x[1].values()), reverse=True)

# Print the Twitter IDs of the most interactive users
print("The most interactive users are:")
for user in sorted_users[:5]:
  print(user[0])
