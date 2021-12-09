import sys
import praw
from datetime import date
import random
import json
import os
import time

reddit = praw.Reddit(
    client_id='2UnDGCqOEVAPBH_40AGM5Q',
    client_secret='xJ_PnfI7GASPqffymTT0cLE7cXVC6Q',
    password='753198624/*-+',
    user_agent='ismail1',
    username='Positive_Square728',
)
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
subName = ''
def get_id_post():
    global list_reddit
    sub_name = ['how_want_comment_','heeelolo']
    sub = random.choice(sub_name)
    global subName
    subName = sub
    subreddit = reddit.subreddit(sub)
    submissions = subreddit.new()
    list_reddit = []
    for submission in submissions:
        list_reddit.append(submission.id)
    return list_reddit


def dataJson():
    print(subName + ' this dumps data')
    with open(subName+'listId.txt', 'w') as json_file:
        json.dump(listReddit, json_file)

def comment():
    global listReddit
    try:
        listReddit = get_id_post()
        data = ''
        print(subName + ' this gets data')
        with open(os.path.join(sys.path[0], subName+'listId.txt'), 'r') as f:
            data = json.load(f)
        list_data = [
            "So Nice. Hope you also check out my NFT´s. I did serveral Collections. CryptobugsClub, CrypticBees, Coinimals and Hugs of Olaf. Let me know if you like them"
            ,
            "Hey, i am new in this. But i found an amazing Artist. Check out Secret NFT Artist on Instagram or Twitter.",
            "Is Elon Musk the Secret NFT Artist? I just saw this Account at Opensea and was wondering if he is behind this. Do you know?"
            , "Check out my Buddy! Secret NFT Artist @Opensea is releasing his NFT´s",
            "NFT Giveaway!!! We are giving away a small part of our CrypticBee Swarm. All you have to do: 🐝 post your ETH Adress in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CrypticBees @opensea 💥good Luck",
            "Catch the Swarm. There are just 222 of these CrypticBees available. Minted by an algorithm 🚀💥🪐 Creator🤖 Secret NFT Artist. Sale at Opensea NFT Giveaway!!! We are giving away a small part of our CryptoBugsClub. All you have to do: 🐝 post your ETH Adresse in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CryptoBugsClub Items @opensea 💥good Luck",
            "Catch the Swarm. There are just 222 of these CrypticBees available. Minted by an algorithm 🚀💥🪐 Creator🤖 Secret NFT Artist. Sale at Opensea NFT Giveaway!!! We are giving away a small part of our CryptoBugsClub. All you have to do: 🐝 post your ETH Adresse in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CryptoBugsClub Items @opensea 💥good Luck",
            "Xmas is on the Way. I created a „Hugs of Olaf“ Collection. Check out the Happy & Scary Olafs @opensea. Gime a Hug and collect one. 🚀💥🪐"]
        for ids in listReddit:
            test = False
            for ids2 in data:
                if ids != ids2:
                    test = True
                else:
                    test = False
                    break
            if test:
                print('commenting on a post in ' + subName)
                comment_random = random.choice(list_data)
                submission = reddit.submission(id=ids)
                submission.reply(comment_random)
                time.sleep(80)

            else:
                print('post already commented on')
        dataJson()
        print('second time gen file ' + subName)

    except:
        listReddit = get_id_post()
        print(subName)
        list_data = [
            "So Nice. Hope you also check out my NFT´s. I did serveral Collections. CryptobugsClub, CrypticBees, Coinimals and Hugs of Olaf. Let me know if you like them"
            ,
            "Hey, i am new in this. But i found an amazing Artist. Check out Secret NFT Artist on Instagram or Twitter.",
            "Is Elon Musk the Secret NFT Artist? I just saw this Account at Opensea and was wondering if he is behind this. Do you know?"
            , "Check out my Buddy! Secret NFT Artist @Opensea is releasing his NFT´s",
            "NFT Giveaway!!! We are giving away a small part of our CrypticBee Swarm. All you have to do: 🐝 post your ETH Adress in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CrypticBees @opensea 💥good Luck",
            "Catch the Swarm. There are just 222 of these CrypticBees available. Minted by an algorithm 🚀💥🪐 Creator🤖 Secret NFT Artist. Sale at Opensea NFT Giveaway!!! We are giving away a small part of our CryptoBugsClub. All you have to do: 🐝 post your ETH Adresse in this Post 🤖Follow @secret_nft_artist on Instagram 🚀Like at least 3 CryptoBugsClub Items @opensea 💥good Luck"]
        for ids in listReddit:
            comment_random = random.choice(list_data)
            submission = reddit.submission(id=ids)
            time.sleep(80)
            submission.reply(comment_random)
        dataJson()
        print('first time gen file ' + subName)


index = 0
while True:
    comment()
    index += 1
    print(index)
