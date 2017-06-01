import os
import re
import time

import praw

print("GrammazNaziBot2k loading...")

print("Bot loaded. Let's correct them!")

reddit = praw.Reddit(
    user_agent    = 'GrammarNaziMachine2k 007 (by /u/SteveCCL)',
    client_id     = os.environ['client_id'],
    client_secret = os.environ['client_secret'],
    username      = os.environ['username'],
    password      = os.environ['password']
)

needs_fix_he_she   = re.compile(r'\b(he\s*(/|\s+or\s+)\s*she|she\s*(/|\s+or\s+)\s*he)\b', re.IGNORECASE)

def generate_reply(comment):
    """Generates a reply base on the comment. Returns None if there shouldn't be a reply"""
    reply = ""
    if re.search(needs_fix_he_she, comment):
        reply += "You may use the *gender-neutral*, *singular* `they` instead of `he/she` when talking about a person with unknown gender.  \nClick [this](https://en.wikipedia.org/wiki/Singular_they) for more info."

    if len(reply) > 0:
        reply += "\n\n^Beep ^blop ^I'm ^a ^bot. ^I ^said ^beep ^blop ^I'm ^a ^bot.  \n^If ^there's ^something ^wrong ^please ^message ^SteveCCL."
        return reply

    return None

while 1:
    try:
        for comment in reddit.subreddit('all').stream.comments():
            if comment.author.name == "GrammarNaziMachine2k":
                continue

            reply = generate_reply(comment.body)
            if reply:
                comment.reply(reply)

    except Exception as e:
        if 'RATELIMIT: ' in str(e):
            t = int(str(e).split(' ')[10])
            print("RATELIMIT exceeded. Sleeping for {} minutes....".format(t))
            time.sleep(60 * t)
        else:
            print("Something went wrong ({})".format(type(e)))
            print(e)
            time.sleep(60)
        print("Resuming")
