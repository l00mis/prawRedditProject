import praw  # official reddit package
from datetime import datetime  # for cakeday

reddit = praw.Reddit(client_id='{client_id}',
                     client_secret='{client_secret}', password='{password}',
                     user_agent='L00mis RedditProject V2', username='{}')
# log in credentials, client id & secrete are from reddit dev
# log in credentials, client id & secrete are from reddit dev

me = str(reddit.user.me())  # logged in /u

#Quick subreddit pointer changes below
esubreddit = reddit.subreddit('explainlikeimfive')  # set the subreddit to run for ELI5
tsubreddit = reddit.subreddit('todayilearned')  # set the subreddit to run for TIL
allsubreddit = reddit.subreddit('all')  # set the subreddit to run for All
rsubreddit = reddit.subreddit('random')  # set the subreddit to run for [Random]

#global post show limits, sets respecitve limit to X posts
elimit = 2 #ELI5
tlimit = 1 #TIL
alllimit = 5 #All
randomlimit = 5 #Random

def intro():
    commentkarma = str(reddit.user.me().comment_karma)  # u/ comment karma
    linkkarma = str(reddit.user.me().link_karma)  # u/ link karma
    cakeday = datetime.utcfromtimestamp(reddit.user.me().created_utc)  # the long datetime string for cakeday
    cakedate = datetime.date(cakeday)  # the date for cakeday

    print("Welcome " + me + ",")
    print("Karma Summary -- Comment:" + commentkarma + " | Link:" + linkkarma)
    print("Redditor Since: " + str(cakedate) + " | " + str(datetime.utcnow().year - cakeday.year) + " cakes consumed")

def getrandomsub():
    rdesc = rsubreddit.public_description  # subreddits public description
    r = str(rsubreddit)  # human name of the subreddit
    rsubcount = "{:,}".format(rsubreddit.subscribers)  # subreddits sub count
    ronline = "{:,}".format(rsubreddit.accounts_active)  # subreddits online in last 15 min count
    nsfwflag = rsubreddit.over18  # boolean for subreddit is/is not safe for work
    hot_random = rsubreddit.hot(limit=randomlimit)  # sets the sort type and limit for posts indexed and returned

    print('--------------------------------------Posts from ???------------------------------------------')
    print("Your Hot 5 random posts from r/: " + r)
    print("Description: " + rdesc)
    print("Subs: " + rsubcount + " | Online Now: " + ronline + "| Is NSFW: " + str(nsfwflag) + "\n")

    for submission in hot_random:
        if not submission.stickied or not rsubreddit.user_is_subscriber:  # not sub to r/ & not sticky post
            print('Title: {}'.format(submission.title))
            print('By: {} | UpVotes:{} | DownVotes:{} | Comments:{}'.format(submission.author,
                                                                            "{:,}".format(submission.ups),
                                                                            "{:,}".format(submission.downs),
                                                                            "{:,}".format(submission.num_comments)))
            print(f'Link: https://reddit.com{submission.permalink}' + "\n")
            # for the limit of hot 5 posts in r/, provide the ^

    sub2r = input("Subscribe to r/" + r + "? | y/n" + "\n").lower()
    if sub2r == 'y':
        reddit.subreddit(r).subscribe()
        print("Successfully subscribed to r/" + r)
    elif sub2r == 'n':
        print("Not Subscribed to r/" + r)
    else:
        print("Use y for Yes, n for No")
    print(sub2r)
    # Checks if the user wants to subscribe to the random subreddit given

    newrand = input("New random (r) or main menu? (mm)")
    if newrand == "r":
        print(getrandomsub())
    elif newrand == "mm":
        print(home())
    else:
        print("Use r for a new random subreddit, or mm to return to the main menu")
    # Checks if the user wants to get a new random subreddit or go back to the home function

def gerallreddit():
    a = str(allsubreddit)
    hot_all = allsubreddit.hot(limit=alllimit)  # sets the sort type and limit for posts indexed and returned

    print('--------------------------------------Posts from r/All------------------------------------------')
    print("Your Hot 5 posts in r/" + a + "\n")
    for submission in hot_all:
        if not submission.stickied:  # not sticky post
            print('Title: {} | Post NSFW? {}'.format(submission.title, submission.over_18))
            print('By: {} | UpVotes:{} | DownVotes:{} | Comments:{}'.format(submission.author,
                                                                            "{:,}".format(submission.ups),
                                                                            "{:,}".format(submission.downs),
                                                                            "{:,}".format(submission.num_comments)))
            print(f'Link: https://reddit.com{submission.permalink}' + "\n")
    # for the limit of hot 5 posts in r/, provide the ^

def todaystil():
    tdesc = tsubreddit.public_description  # subreddits public description
    t = str(tsubreddit)  # human name of the subreddit
    tsubcount = "{:,}".format(tsubreddit.subscribers)  # subreddits sub count
    tonline = "{:,}".format(tsubreddit.accounts_active)  # subreddits online in last 15 min count
    top_til = tsubreddit.top(limit=tlimit)  # sets the sort type and limit for posts indexed and returned
    print('Here is ' + me + "'s TIL fact of the day:")
    print(tdesc + "\n" + '/r:' + t + ' (TIL) has ' + tonline + ' redditors online of ' + tsubcount + ' subscribers' + "\n")
    for submission in top_til:
        if not submission.stickied:  # not sticky post
            print('Title: {}'.format(submission.title))
            print('By: {} | Post NSFW? {} | UpVotes:{} | DownVotes:{} | Comments:{}'.format(submission.author,
                                                                                            submission.over_18,
                                                                                            "{:,}".format(
                                                                                                submission.ups),
                                                                                            "{:,}".format(
                                                                                                submission.downs),
                                                                                            "{:,}".format(
                                                                                                submission.num_comments)))
            print(f'Link: https://reddit.com{submission.permalink}' + "\n")
    # for the limit of hot 5 posts in r/til, provide the ^

def todayseil5():
    edesc = esubreddit.public_description  # subreddits public description
    e = str(esubreddit)  # human name of the subreddit
    esubcount = "{:,}".format(esubreddit.subscribers)  # subreddits sub count
    eonline = "{:,}".format(esubreddit.accounts_active)  # subreddits online in last 15 min count
    top_til = esubreddit.top(limit=elimit)  # sets the sort type and limit for posts indexed and returned
    print('Here is ' + me + "'s TIL fact of the day:")
    print('/r:' + e + ' (ELI5) has ' + eonline + ' redditors online of ' + esubcount + ' subscribers' + "\n")
    for submission in top_til:
        if not submission.stickied:  # not sticky post
            print('Title: {}'.format(submission.title))
            print('By: {} | Post NSFW? {} | UpVotes:{} | DownVotes:{} | Comments:{}'.format(submission.author,
                                                                                            submission.over_18,
                                                                                            "{:,}".format(
                                                                                                submission.ups),
                                                                                            "{:,}".format(
                                                                                                submission.downs),
                                                                                            "{:,}".format(
                                                                                                submission.num_comments)))
            print(f'Link: https://reddit.com{submission.permalink}' + "\n")
    # for the limit of hot 5 posts in r/til, provide the ^

def home():
    mmm = "What would you like to see?" + "\n"
    helptxt = "\n" + "Main Menu" + "\n" + "Selections: all/a | til/t | eil5/e/5 | random/r | new | end"
    print(helptxt)
    while True:
        main_menu = input(mmm).lower()
        if main_menu == "all" or main_menu == "a":
            print(gerallreddit())
            print(home())
        elif main_menu == "til" or main_menu == "t":
            print(todaystil())
            print(home())
        elif main_menu == "eil5" or main_menu == "e" or main_menu == "5":
            print(todayseil5())
            print(home())
        elif main_menu == "random" or main_menu == "r":
            print(getrandomsub())
        elif main_menu == "new":
            print(intro())
        elif main_menu == "end":
            break
        else:
            print("Invalid Input. Try things like: all/a | til/t | eil5/e/5 | random/r")
            print(main_menu())

intro()
home()

# Created by /u/L00mis

#See Github @ https://github.com/l00mis/prawRedditProject

# resources below
# https://praw.readthedocs.io/en/latest/code_overview/models/redditor.html#praw.models.Redditor
# https://github.com/reddit-archive/reddit/wiki/JSON
# https://www.reddit.com/dev/api
# https://praw.readthedocs.io/en/latest/getting_started/authentication.html
# https://praw.readthedocs.io/en/v3.6.2/pages/useful_scripts.html
# https://www.reddit.com/r/redditdev/comments/h03b0p/getting_link_comment_karma/?
# https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
