import time
import praw
import random

reddit2 = praw.Reddit(
    client_id='2owIcRaKwx4gbVU_DTd3JQ',
    client_secret='9qeJ66kH066TMBJhDkMgUMjxwjOgaQ',
    password='753198624/*-+',
    user_agent='ismail1',
    username='CharacterAnybody8800',
)
reddit3 = praw.Reddit(
    client_id='DZfwXx8b7_8dAxSj8rpwnw',
    client_secret='b67eih-NrrfTCUkMDUZPvZKt3JBVVQ',
    password='n3F*YWe#gm~A&z',
    user_agent='ismail2',
    username='Worldly_Respect7090',
)

list_reddit_account = [reddit2]
url = input("give me your url :")

reddit = random.choice(list_reddit_account)
ID = url.split('/')[-3]


def get_id_post():
    print("the id of the post is : " + str(ID))
    submission = reddit.submission(id=str(ID))
    title = submission.title
    print("the title of the post is : " + str(title))


def fast_upvote():
    count = 0
    number = int(input("how much the number of upvote you need : "))
    for x in list_reddit_account:
        submission = x.submission(id=str(ID))
        if count < number:
            print(x.user.me())
            submission.upvote()
            count += 1
            time.sleep(60)
        else:
            print("done")
            break


def slow_upvote():
    count = 0
    number = int(input("how much the number of upvote you need : "))
    for x in list_reddit_account:
        submission = x.submission(id=str(ID))
        if count < number:
            print(x.user.me())
            submission.upvote()
            count += 1
            time.sleep(3600)
        else:
            print("done")
            break


def main():
    chose = input("which of the method you need cheese the slow out the fast")
    if chose == "fast":
        get_id_post()
        fast_upvote()
    elif chose == "slow":
        get_id_post()
        slow_upvote()
    else:
        print("give me what do you want ")


main()
