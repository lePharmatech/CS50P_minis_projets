import random

# coin = random.choice(["head","tails"])
# print(coin)

# from random import choice
# coin = choice(["head","tails"])
# print(coin)

aleatoire = random.randint(1, 10)
print(aleatoire)

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)
