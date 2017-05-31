import os
import re
import time

import praw

print("GrammazNaziBot2k loading...")

corrected = int(os.getenv('corrected', '0'))

print("Already corrected {} people.".format(corrected))
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

try:
    while 1:
        try:
            for comment in reddit.subreddit('all').stream.comments():
                if re.search(needs_fix_he_she, comment.body):
                    comment.reply("You may use the *gender-neutral*, *singular* `they` when talking about a person with unknown gender.  \nClick [this](https://en.wikipedia.org/wiki/Singular_they) for more info.  \nI've corrected {} people before you.\n\n^Beep ^blop ^I'm ^a ^bot. ^I ^said ^beep ^blop ^I'm ^a ^bot.  \n^If ^there's ^something ^wrong ^please ^message ^SteveCCL.".format(corrected))
                    corrected += 1
                    print("Corrected #{}, {} ({})".format(corrected, comment.author.name, comment))
                    os.environ['corrected'] = str(corrected)
                elif re.search(needs_fix_his_hers, comment.body):
                    comment.reply("You may use the *gender-neutral*, *singular* `their` when talking about a person with unknown gender.  \nClick [this](https://en.wikipedia.org/wiki/Singular_they) for more info.  \nI've corrected {} people before you.\n\n^Beep ^blop ^I'm ^a ^bot. ^I ^said ^beep ^blop ^I'm ^a ^bot.  \n^If ^there's ^something ^wrong ^please ^message ^SteveCCL.".format(corrected))
                    corrected += 1
                    print("Corrected #{}, {} ({})".format(corrected, comment.author.name, comment))
                    os.environ['corrected'] = str(corrected)

        except Exception as e:
            print("Something went wrong ({})".format(type(e)))
            print(e)
            time.sleep(60)
            print("Resuming")
except KeyboardInterrupt:
    print("User requested termination")

print("See you soon")
