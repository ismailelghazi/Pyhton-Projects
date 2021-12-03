import time
import praw
from datetime import date
import random

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
# subreddit = reddit.subreddit("PixelArt")
subreddit = reddit.subreddit("how_want_comment_")
right_now = subreddit.hot()
def get_id_post():
    list_reddit = []
    for submission in right_now:
            # date1 = datetime.datetime.fromtimestamp(submission.created_utc).strftime("%Y-%m-%d")
            # print(submission.title + "***" + submission.id + "***" + date1)
            list_reddit.append(submission.id)
    for tes in list_reddit:
        print(tes)
    return list_reddit

get_id_post()
def commint():
    list_data = ["So Nice. Hope you also check out my NFT´s. I did serveral Collections. CryptobugsClub, CrypticBees, Coinimals and Hugs of Olaf. Let me know if you like them"
                 ,"Hey, i am new in this. But i found an amazing Artist. Check out Secret NFT Artist on Instagram or Twitter.",
                 "Is Elon Musk the Secret NFT Artist? I just saw this Account at Opensea and was wondering if he is behind this. Do you know?"
                 ,"Check out my Buddy! Secret NFT Artist @Opensea is releasing his NFT´s",
                 "NFT Giveaway!!! We are giving away a small part of our CrypticBee Swarm. All you have to do: 🐝 post your ETH Adress in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CrypticBees @opensea 💥good Luck",
                 "Catch the Swarm. There are just 222 of these CrypticBees available. Minted by an algorithm 🚀💥🪐 Creator🤖 Secret NFT Artist. Sale at Opensea NFT Giveaway!!! We are giving away a small part of our CryptoBugsClub. All you have to do: 🐝 post your ETH Adresse in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CryptoBugsClub Items @opensea 💥good Luck"]
    comment_rondam = random.choice(list_data)
    for my_comment in get_id_post():
        submission = reddit.submission(my_comment)
        submission.award(message=comment_rondam)
def main():
    get_id_post()
    commint()
limit = 0
while limit == 0:
    main()
    time.sleep(10)
     # time.sleep(60)