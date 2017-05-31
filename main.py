import praw
import client_data

reddit = praw.Reddit(
    user_agent    = "GrammarNaziMachine2k 007 (by /u/SteveCCL",
    client_id     = client_data.client_id,
    client_secret = client_data.client_secret,
    username      = client_data.username,
    password      = client_data.password
    )

for comment in reddit.subreddit('all').stream.comments():
    print(comment)
    break
