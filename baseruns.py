h = input("Insert how many hits: ")
bb = input("Insert how many walks: ")
hr = input("Insert how many home runs: ")
tb = input("Insert the amount of total bases: ")
ab = input("Insert the amount of at bats: ")

a = h + bb - hr
b = (1.4 * tb - .6 * h - 3 * hr + .1 * bb) * 1.02
c = ab - h
d = hr

result = (a * b) / (b + c) + d

print result

