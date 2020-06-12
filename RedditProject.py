import praw  # official reddit package
from datetime import datetime  # for cakeday

reddit = praw.Reddit(client_id='{client_id}',
                     client_secret='{client_secret}', password='{user_password}',
                     user_agent='{an identifiable text string for whay your doing}', username='{user_name}')
#log in credentials, client id & secrete are from reddit dev

me = str(reddit.user.me())  # logged in /u
commentkarma = str(reddit.user.me().comment_karma)  # u/ comment karma
linkkarma = str(reddit.user.me().link_karma)  # u/ link karam
cakeday = datetime.utcfromtimestamp(reddit.user.me().created_utc)  # the long datetime string for cakeday
cakedate = datetime.date(cakeday)  # the date for cakeday
print("Welcome " + me + ",")
print("Karma Summary -- Comment:" + commentkarma + " | Link:" + linkkarma)
print("Redditor Since: " + str(cakedate) + " | " + str(datetime.utcnow().year - cakeday.year) + " cakes")

RSubReddit = reddit.subreddit('random')  # set the subreddit to run for
rdesc = RSubReddit.public_description  # subreddits public description
r = str(RSubReddit)  # human name of the subreddit
rsubsribers = "{:,}".format(RSubReddit.subscribers)  # subreddits sub count
ronline = "{:,}".format(RSubReddit.accounts_active)  # subreddits online in last 15 min count
NSFWFlag = RSubReddit.over18  # boolean for subreddit is/is not safe for work
hot_random = RSubReddit.hot(limit=5)  # sets the sort type and limit for posts indexed and returend

print('--------------------------------------Posts from ???------------------------------------------')
print("Your Hot 5 random posts from r/: " + r)
print("Description: " + rdesc)
print("Subs: " + rsubsribers + " | Online Now: " + ronline + "| Is NSFW: " + str(NSFWFlag) + "\n")

for submission in hot_random:
    if not submission.stickied or not RSubReddit.user_is_subscriber:  # not sub to r/ & not sticky post
        print('Title: {}'.format(submission.title))
        print('By: {} | UpVotes:{} | DownVotes:{} | Comments:{}'.format(submission.author,
                                                                        "{:,}".format(submission.ups),
                                                                        "{:,}".format(submission.downs),
                                                                        "{:,}".format(submission.num_comments)))
        print(f'Link: reddit.com{submission.permalink}' + "\n")
# for the limit of hot 5 posts in r/, provide the ^

# Starting All
allsubreddit = reddit.subreddit('all')  # set the subreddit to: r/all
a = str(allsubreddit)
hot_all = allsubreddit.hot(limit=5)  # sets the sort type and limit for posts indexed and returend

print('--------------------------------------Posts from r/All------------------------------------------')
print("Your Hot 5 posts in r/" + a + "\n")
for submission in hot_all:
    if not submission.stickied:
        print('Title: {} | Post NSFW? {}'.format(submission.title, submission.over_18))
        print('By: {} | UpVotes:{} | DownVotes:{} | Comments:{}'.format(submission.author,
                                                                        "{:,}".format(submission.ups),
                                                                        "{:,}".format(submission.downs),
                                                                        "{:,}".format(submission.num_comments)))
        print(f'Link: reddit.com{submission.permalink}' + "\n")
# for the limit of hot 5 posts in r/, provide the ^

# Created by L00mis

# resources below
# https://praw.readthedocs.io/en/latest/code_overview/models/redditor.html#praw.models.Redditor
# https://github.com/reddit-archive/reddit/wiki/JSON
# https://www.reddit.com/dev/api
# https://praw.readthedocs.io/en/latest/getting_started/authentication.html
# https://praw.readthedocs.io/en/v3.6.2/pages/useful_scripts.html
# https://www.reddit.com/r/redditdev/comments/h03b0p/getting_link_comment_karma/?
