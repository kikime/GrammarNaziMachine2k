import client_data

import praw
import re
import sys

print("GrammazNaziBot2k loading...")

corrected = 0
with open("db.txt") as f:
    try:
        corrected = int(f.read_line())
    except ValueError:
        print("Error reading db.txt. Assuming 0 corrected people.")
        corrected = 0

print("Already corrected {} people.")
print("Bot loaded. Let's correct them!")

needs_fix_he_she   = re.compile(r'(he\s*(/|\s+or\s+)\s*she|she\s*(/|\s+or\s+)\s*he)', re.IGNORECASE)
needs_fix_his_hers = re.compile(r'(his\s*(/|\s+or\s+)\s*hers|hers\s*(/|\s+or\s+)\s*his)', re.IGNORECASE)

reddit = praw.Reddit(
    user_agent    = 'GrammarNaziMachine2k 007 (by /u/SteveCCL)',
    client_id     = client_data.client_id,
    client_secret = client_data.client_secret,
    username      = client_data.username,
    password      = client_data.password
)

try:
    for comment in reddit.subreddit('all').stream.comments():
        if re.search(needs_fix_he_she, comment.body):
            print("Found he/she")
            print(comment)
        elif re.search(needs_fix_his_hers, comment.body):
            print("Found his/hers")
            print(comment)
except KeyboardInterrupt:
    print("User requested termination")

except:
    print("Something went wrong")
