import praw
from datetime import date
import datetime

reddit2 = praw.Reddit(
    client_id='2owIcRaKwx4gbVU_DTd3JQ',
    client_secret='9qeJ66kH066TMBJhDkMgUMjxwjOgaQ',
    password='753198624/*-+',
    user_agent='ismail1',
    username='CharacterAnybody8800',
)
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
reddit = reddit2
subreddit = reddit.subreddit("PixelArt")
right_now = subreddit.new()
list_reddit = []
while 1:
        for submission in right_now:
            date1 = datetime.datetime.fromtimestamp(submission.created_utc).strftime("%Y-%m-%d")
            print(submission.title + "***" + submission.id + "***" + date1)
            list_reddit.append(submission.id)
numbre = 1
for test in list_reddit:
    print(test +" "+str(numbre))
    numbre+=1