__author__ = 'akaash'

for z in range(1, 101, 1):
    if z % 3 == 0 and z % 5 == 0:
        print "fizzbuzz"
    elif z % 3 == 0:
        print "fizz"
    elif z % 5 == 0:
        print "buzz"
    else:
        print z
