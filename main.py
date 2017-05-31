import client_data

import praw
import re
import time

print("GrammazNaziBot2k loading...")

corrected = 0
try:
    with open("db.txt", 'r') as f:
        try:
            corrected = int(f.readline())
        except ValueError:
            print("Error reading db.txt. Assuming 0 corrected people.")
except FileNotFoundError:
    print("db.txt not found.")
    print("Creating it.")
    with open("db.txt", 'w') as f:
        f.write('0\n')

print("Already corrected {} people.".format(corrected))
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
    while 1:
        try:
            for comment in reddit.subreddit('all').stream.comments():
                if re.search(needs_fix_he_she, comment.body):
                    comment.reply("You may use the *gender-neutral*, *singular* `they` when talking about a person with unknown gender.  \nClick [this](https://en.wikipedia.org/wiki/Singular_they) for more info.  \nI've corrected {} people before you.\n\n^Beep ^blop ^I'm ^a ^bot. ^I ^said ^beep ^blop ^I'm ^a ^bot.  \n^If ^there's ^something ^wrong ^please ^message ^SteveCCL.".format(corrected))
                    corrected += 1
                    print("Corrected #{}, {} ({})".format(corrected, comment.author.name, comment))
                elif re.search(needs_fix_his_hers, comment.body):
                    comment.reply("You may use the *gender-neutral*, *singular* `their` when talking about a person with unknown gender.  \nClick [this](https://en.wikipedia.org/wiki/Singular_they) for more info.  \nI've corrected {} people before you.\n\n^Beep ^blop ^I'm ^a ^bot. ^I ^said ^beep ^blop ^I'm ^a ^bot.  \n^If ^there's ^something ^wrong ^please ^message ^SteveCCL.".format(corrected))
                    corrected += 1
                    print("Corrected #{}, {} ({})".format(corrected, comment.author.name, comment))

        except:
            print("Something went wrong")
            time.sleep(60)
            print("Resuming")
except KeyboardInterrupt:
    print("User requested termination")

with open("db.txt", 'w') as f:
    f.write(str(corrected))

print("See you soon")
