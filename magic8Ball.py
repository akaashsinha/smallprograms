__author__ = 'akaash'
import random
import time
import sys
import os

# Magic 8 Ball

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
           "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
           "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
           "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

question = raw_input("What is your question? ")
print "I am thinking..."
time.sleep(1)

# I learned about the choice command from the random module, much better than picking a random int
answer = random.choice(answers)
print answer

results = input("Press 1 to save your results ")

if results == 1:
    desktop = os.path.expanduser("~/Desktop/Magic_8_Ball.txt")
    results = open(desktop, 'a')
    results.write('Question: %s Answer: %s \n' % (question, answer))
    results.close()

else:
    sys.exit()


