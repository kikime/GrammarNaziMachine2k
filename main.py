import os
import re
import time

import praw

LOG_LEVEL = 2

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
needs_fix_they_is  = re.compile(r'\bthey\s+is', re.IGNORECASE)

def generate_reply(comment):
    """Generates a reply based on the comment. Returns None if there shouldn't be a reply"""
    reply = ""
    if re.search(needs_fix_he_she, comment):
        reply += "You may use the *gender-neutral*, *singular* `they` instead of `he/she` when talking about a person with unknown gender.  \nClick [this](https://en.wikipedia.org/wiki/Singular_they) for more info.\n\n"
        if LOG_LEVEL > 1:
            print("he_she")

    if "plug-out" in comment:
        reply += "It's `unplug` not `plug-out` even though I commend you for using that.\n\n"
        if LOG_LEVEL > 1:
            print("plug-out")

    if re.search(needs_fix_they_is, comment):
        reply += "It's `they are` or `they're` not `they is`.\n\n"
        if LOG_LEVEL > 1:
            print("they is")

    if "excepted" in comment:
        reply += "It's `accepted` not `excepted`.\n\n"
        if LOG_LEVEL > 1:
            print("excepted")

    if len(reply) > 0:
        reply += "^Beep ^blop ^I'm ^a ^bot. ^I ^said ^beep ^blop ^I'm ^a ^bot.  \n^If ^there's ^something ^wrong ^please ^message ^SteveCCL."
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
