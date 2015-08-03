__author__ = 'akaash'
import random
# This program is a product of a shower thought

# These are the most common first names of 2015 from here http://bit.ly/1vGLoGu
firstNames = ['Sophia', 'Emma', 'Olivia', 'Ava', 'Isabella', 'Mia', 'Zoe', 'Lily', 'Emily', 'Madelyn',
              'Jackson', 'Aiden', 'Liam', 'Lucas', 'Noah', 'Mason', 'Ethan', 'Caden', 'Jacob', 'Logan']

# These are the most common last names in the US according to here http://bit.ly/1ilxZdK
lastNames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez',
             'Rodriguez', 'Wilson', 'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore',
             'Martin', 'Jackson', 'Thompson', 'White']


print firstNames[random.randint(0, 19)], lastNames[random.randint(0, 19)]
