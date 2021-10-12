# import praw
# import datetime
# reddit = praw.Reddit(
#     client_id='xCQgBw-kL-Dh6ceO12hLPg',
#     client_secret='CW9QeOa_VMhAmnRWDBjpwD_aaWYpMQ',
#     password='jtQy+*$&p^eYQP3',
#     user_agent='ismail',
#     username='ismailELghazi',
# )
# count = 0
# count1 = 0
# word = ["griffiths", "review", "course", "courses"]
# subreddit = reddit.subreddit('GAMSAT')
# hot_python = subreddit.new(limit=5)
# for subm in hot_python:
#     bool = True
#     subreddit_title = subm.title
#     subreddit_text = subm.selftext
#     date = datetime.datetime.fromtimestamp(subm.created_utc)
#     dif = datetime.datetime.utcnow() - date
#     # for time in dif :
#     #     if
#     for test in word:
#         if subreddit_title.find(test) != -1 or subreddit_text.find(test) != -1:
#             print("*******")
#             bool = False
#             count1+=1
#             break
#     if bool == True:
#         print("title :{}  \ndate : {}\ntext: {}".format(subm.title, datetime.datetime.fromtimestamp(subm.created_utc).strftime('%Y-%m-%d'), subm.selftext[:10000000000000]))
#         count += 1
#
# print( "number the post used : "+str(count))
# print( "number the post no used : "+str(count1))
import praw
import datetime
reddit = praw.Reddit(
    client_id='xCQgBw-kL-Dh6ceO12hLPg',
    client_secret='CW9QeOa_VMhAmnRWDBjpwD_aaWYpMQ',
    password='jtQy+*$&p^eYQP3',
    user_agent='ismail',
    username='ismailELghazi',
)
count = 0
count1 = 0
word = ["griffiths", "review", "course", "courses"]
subreddit = reddit.subreddit('GAMSAT')
hot_python = subreddit.new(limit=250000)
for subm in hot_python:
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
    if bool == True:
        print("title :{}  \ndate : {}\ntext: {}".format(subm.title, datetime.datetime.fromtimestamp(subm.created_utc).strftime('%Y-%m-%d'), subm.selftext[:10000000000000]))
        count += 1

print("number the post used : "+str(count))
print("number the post no used : "+str(count1))


