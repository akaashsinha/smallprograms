__author__ = 'akaash'
import random
import time
import sys
import os
from colorama import Fore


# Magic 8 Ball

answers = [Fore.GREEN + "It is certain", Fore.GREEN + "It is decidedly so",
           Fore.GREEN + "Without a doubt", Fore.GREEN + "Yes definitely", Fore.GREEN + "You may rely on it", Fore.GREEN +
           "As I see it, yes", Fore.GREEN + "Most likely", Fore.GREEN + "Outlook good",Fore.GREEN +  "Yes", Fore.GREEN + "Signs point to yes",
           Fore.BLUE + "Reply hazy try again",  Fore.BLUE +
           "Ask again later", Fore.BLUE + "Better not tell you now", Fore.BLUE + "Cannot predict now",  Fore.BLUE +
           "Concentrate and ask again",
           Fore.RED + "Don't count on it", Fore.RED + "My reply is no", Fore.RED + "My sources say no", Fore.RED + "Outlook not so good",
           Fore.RED + "Very doubtful"]

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

