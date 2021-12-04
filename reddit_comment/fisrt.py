import time
import praw
from datetime import date
import random

reddit = praw.Reddit(
    client_id='tuxe1nwe4PIyxARKSCYfoA',
    client_secret='NGUmHTvdBDSBpvhBLpetFTyjJFdAxA',
    password='753198624/*-+',
    user_agent='ismail1',
    username='Positive_Square728',
)
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
SUB_NAME = 'how_want_comment_'


def get_id_post():
    subreddit = reddit.subreddit(SUB_NAME)
    submissions = subreddit.hot()
    list_reddit = []
    for submission in submissions:
        # date = datetime.datetime.fromtimestamp(submission.created_utc).strftime("%Y-%m-%d")
        # print(submission.title + "***" + submission.id + "***" + date)
        list_reddit.append(submission.id)
    return list_reddit
print(get_id_post())
get_id_post()
def comment():
    list_data = ["So Nice. Hope you also check out my NFT´s. I did serveral Collections. CryptobugsClub, CrypticBees, Coinimals and Hugs of Olaf. Let me know if you like them"
                 ,"Hey, i am new in this. But i found an amazing Artist. Check out Secret NFT Artist on Instagram or Twitter.",
                 "Is Elon Musk the Secret NFT Artist? I just saw this Account at Opensea and was wondering if he is behind this. Do you know?"
                 ,"Check out my Buddy! Secret NFT Artist @Opensea is releasing his NFT´s",
                 "NFT Giveaway!!! We are giving away a small part of our CrypticBee Swarm. All you have to do: 🐝 post your ETH Adress in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CrypticBees @opensea 💥good Luck",
                 "Catch the Swarm. There are just 222 of these CrypticBees available. Minted by an algorithm 🚀💥🪐 Creator🤖 Secret NFT Artist. Sale at Opensea NFT Giveaway!!! We are giving away a small part of our CryptoBugsClub. All you have to do: 🐝 post your ETH Adresse in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CryptoBugsClub Items @opensea 💥good Luck"]
    for ids in get_id_post():
        comment_random = random.choice(list_data)
        print(comment_random)
        print("eee")
        submission = reddit.submission(id=ids)
        print("aaa")
        submission.reply(comment_random)

comment()