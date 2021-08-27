import random


def delai_cart():
    cart = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    carts=random.choice(cart)
    return carts
computer_carts=[]
player_carts=[]
for c in range(2):
    computer_carts.append(delai_cart())
    player_carts.append(delai_cart())
def calcul_score(cart):
    return sum(cart)