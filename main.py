import os
import re
import time

import praw

print("GrammazNaziBot2k loading...")

print("Bot loaded. Let's correct them!")

needs_fix_he_she   = re.compile(r'\b(he\s*(/|\s+or\s+)\s*she|she\s*(/|\s+or\s+)\s*he)\b', re.IGNORECASE)
needs_fix_his_hers = re.compile(r'\b(his\s*(/|\s+or\s+)\s*hers|hers\s*(/|\s+or\s+)\s*his)\b', re.IGNORECASE)

reddit = praw.Reddit(
    user_agent    = 'GrammarNaziMachine2k 007 (by /u/SteveCCL)',
    client_id     = os.environ['client_id'],
    client_secret = os.environ['client_secret'],
    username      = os.environ['username'],
    password      = os.environ['password']
)

def generate_reply(comment):
    return None

while 1:
    try:
        for comment in reddit.subreddit('all').stream.comments():
            if comment.author.name == "GrammarNaziMachine2k":
                continue
            """
            if re.search(needs_fix_he_she, comment.body):
                comment.reply("You may use the *gender-neutral*, *singular* `they` instead of `he/she` when talking about a person with unknown gender.  \nClick [this](https://en.wikipedia.org/wiki/Singular_they) for more info.\n\n^Beep ^blop ^I'm ^a ^bot. ^I ^said ^beep ^blop ^I'm ^a ^bot.  \n^If ^there's ^something ^wrong ^please ^message ^SteveCCL.".format(corrected))
                corrected += 1
                print("Corrected #{}, {} ({})".format(corrected, comment.author.name, comment))
                os.environ['corrected'] = str(corrected)
            elif re.search(needs_fix_his_hers, comment.body):
                comment.reply("You may use the *gender-neutral*, *singular* `their` instead of `his/hers` when talking about a person with unknown gender.  \nClick [this](https://en.wikipedia.org/wiki/Singular_they) for more info.\n\n^Beep ^blop ^I'm ^a ^bot. ^I ^said ^beep ^blop ^I'm ^a ^bot.  \n^If ^there's ^something ^wrong ^please ^message ^SteveCCL.".format(corrected))
                corrected += 1
                print("Corrected #{}, {} ({})".format(corrected, comment.author.name, comment))
                os.environ['corrected'] = str(corrected)
            """

    except Exception as e:
        if 'RATELIMIT: ' in str(e):
            t = int(str(e).split(' ')[10])
            print("RATELIMIT exceeded. Sleeping for {}....".format(t))
            time.sleep(60 * t)
        else:
            print("Something went wrong ({})".format(type(e)))
            print(e)
            time.sleep(60)
        print("Resuming")
