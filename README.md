# prawRedditProject
A project for learning python while using Reddit's praw API.

For starters, I am 100% self taught and started learning python when I lost my job. This is the result of a few weeks of reading, testing and playing with suggested projects on Reddit. I have also compiled a list of links for other project ideas, see the other projects files for ideas.

How I started this project: I wanted to pull a random subreddit and see the hot 5 posts, so I looked at praw and started to play around with it in pycharmCE. After creating a Reddit authorized application in preferences > apps > 'create another app...'. this will allow you to get the ids needed in the script. The secrete is shown when you click edit, and the client id is in the upper right of the developed applications card for your app.

**When creating a new app use: http://localhost:8080 for the redirect uri**

Once that was created, the first thing I did was make a way to produce the top 5 hot posts from a random subreddit and pint the results. I added a print for the username that was logging in and that was V1 in the bag. But that wasn't enough, so I looked for ways to expand. I added r/all, removing the not sticky condition along the way, and added some more details about the logged in users karma and cakeday.

Adding complexity, the next step was to create functions and move thought the scripts in a more user friendly way than printing 10 links. I also wanted the ability to sub to the random Reddits that were presented, and loop for the ability to refresh new random r/'s or return to the menu to see u/ karma & cake details or navigate to r/all, and soon to add TIL & ELI5 top post of the day as their own functions and menu options.

After adding the loops and new subreddits, I will # the posts as they print so they are visually easier to identiy the breaks.

# -- Change Log -- 
1.0 Base random Reddit generator w/ user login via praw API 
1.1 added r/all and karma/cakeday details 
2.0 restructure of file and created definitions for each portion. TIL/ELI5 Facts 
2.1 addded start menu for selecting r/ and changing selection, moved pointers and limits to globals 

# -- Feature Road Map -- 
2.X Numbered list for links printed (1-5) 

# -- Resources -- 
https://praw.readthedocs.io/en/latest/code_overview/models/redditor.html#praw.models.Redditor
https://github.com/reddit-archive/reddit/wiki/JSON
https://www.reddit.com/dev/api
https://praw.readthedocs.io/en/latest/getting_started/authentication.html
https://praw.readthedocs.io/en/v3.6.2/pages/useful_scripts.html
https://www.reddit.com/r/redditdev/comments/h03b0p/getting_link_comment_karma/?
https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
