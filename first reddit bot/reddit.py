import praw
reddit = praw.Reddit(
    client_id='xCQgBw-kL-Dh6ceO12hLPg',
    client_secret='CW9QeOa_VMhAmnRWDBjpwD_aaWYpMQ',
    password='jtQy+*$&p^eYQP3',
    user_agent='ismail',
    username='ismailELghazi',
)
count = 0
word = ["griffiths", "review", "course", "courses", "DDS"]
subreddit = reddit.subreddit('GAMSAT')
hot_python = subreddit.new()
for subm in hot_python:
    bool = True
    subreddit_title = subm.title
    subreddit_text = subm.selftext
    for test in word:
        if subreddit_title.find(test) != -1 or subreddit_text.find(test) != -1:
            print("*******")
            bool = False
            break
    if bool == True:
        print("title :{} \ntext: {}\n".format(subm.title, subm.selftext[:10000000000000]))
        count += 1
print(count)
