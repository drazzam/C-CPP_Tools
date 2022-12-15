import tweepy
from textblob import TextBlob
import xlsxwriter

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

# Create an Excel file and write the results to it
workbook = xlsxwriter.Workbook("tweet_results.xlsx")
worksheet = workbook.add_worksheet()

# Write the trends to the first column
worksheet.write("A1", "Trends")
row = 1
col = 0
for trend, count in trends.items():
    worksheet.write(row, col, f"{trend}: {count}")
    row += 1

# Write the most interactive accounts to the second column
worksheet.write("B1", "Most interactive accounts")
row = 1
col = 1
for account, count in accounts.items():
    worksheet.write(row, col, f"{account}: {count}")
    row += 1

# Save the Excel file
workbook.close()
