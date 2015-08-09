__author__ = 'akaash'
# Did this program out of whim and really had no idea what if what I was doing was working, and had an amazing feeling
# When it worked as I expected.

# This program simulates flipping a coin and lets you create multiple instances of coins
# To edit this program just change createCoins to however many coins you want


import random

class Coin(object):
    def __init__(self):
        self.state = "Heads"

    def toss(self):
        number = random.randrange(0,2,1)
        if number == 1:
            self.state = "Heads"
            print "Heads"
        else:
            self.state = "Tails"
            print "Tails"

wallet = list()


def createCoins(x):
    for z in range(x):
        wallet.append(Coin())

# Has to be a list
def rollCoins(coins):
    for z in coins:
        z.toss()

createCoins(5)

rollCoins(wallet)
