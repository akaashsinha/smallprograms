# This program calculates CPI. Measures inflation for price level for market basket. 

price1 = input("What is the base value? ")
price2 = input("What is the new value? ")

cpi = (price2/price1) * 100
print cpi
print "the rate of inflation was: ",  cpi - 100