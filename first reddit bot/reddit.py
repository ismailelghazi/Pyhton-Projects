import time
import random
import praw
import datetime
reddit1 = praw.Reddit(
    client_id='xCQgBw-kL-Dh6ceO12hLPg',
    client_secret='CW9QeOa_VMhAmnRWDBjpwD_aaWYpMQ',
    password='jtQy+*$&p^eYQP3',
    user_agent='ismail',
    username='ismailELghazi',
)
reddit2 = praw.Reddit(
    client_id='WedJ5sB0CVd_eUSvTSNbQA',
    client_secret='oa5qu9AyuUyV5uRhPQzKLW1j8mT3hg',
    password='753198624/*-+',
    user_agent='ismail1',
    username='pic1pac',
)
reddit3 = praw.Reddit(
    client_id='DZfwXx8b7_8dAxSj8rpwnw',
    client_secret='b67eih-NrrfTCUkMDUZPvZKt3JBVVQ',
    password='n3F*YWe#gm~A&z',
    user_agent='ismail2',
    username='Worldly_Respect7090',
)
reddit4 = praw.Reddit(
    client_id='TUFR9f8W_FAurar-1TGzbA',
    client_secret='yEenUjybvVN-XF6ErFLVeZ230kwy9Q',
    password='n3F*YWe#gm~A&z',
    user_agent='ismail3',
    username='Party_Spring_9640',
)
reddit5 = praw.Reddit(
    client_id='h0qK_8VxiKiWPZx735EXEw',
    client_secret='eGYro3Q6_wz-RZQ9cJ1_4LI46s4pbQ',
    password='n3F*YWe#gm~A&z',
    user_agent='ismail4',
    username='Amazing-Broccoli-543',
)
list_reddit_account = [reddit5, reddit3, reddit2, reddit4, reddit1]
reddit = random.choice(list_reddit_account)
print(reddit.user.me())
print(reddit)
count = 0
count1 = 0
word = ["griffiths", "review", "course", "courses"]
subreddit = reddit.subreddit('GAMSAT')
hot_python = subreddit.new(limit=50)
for subm in hot_python:
    interval = time.time() - 60 * 60 * 24 * 7
    interval_month = time.time() - 60 * 60 * 24 * 30 * 2
    bool = True
    subreddit_title = subm.title
    subreddit_text = subm.selftext
    date1 = datetime.datetime.fromtimestamp(subm.created_utc).strftime("%Y-%m-%d")

    for test in word:
        if subreddit_title.find(test) != -1 or subreddit_text.find(test) != -1:
            print("*******")
            bool = False
            count1 += 1
            break
    if bool == True and subm.created_utc <interval and subm.created_utc >interval_month:
        print("title :{}  \ndate : {}\ntext: {}".format(subm.title, datetime.datetime.fromtimestamp(subm.created_utc).strftime('%Y-%m-%d'), subm.selftext))
        count += 1

print("number the post used : "+str(count))
print("day"+str(interval))
# print("month"+str(interval_month))
print("number the post no used : "+str(count1))
