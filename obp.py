h = input("Insert how many hits he had? ")
bb = input("Insert how many walks he had? ")
hbp = input("Insert how many times he got hit by a pitch? ")
ab = input("Insert how many at bats did he have? ")
sf = input("Insert how many sacrifice flies did he have? ")

ob1 =  h + bb + hbp 
ob2 = ab + bb + hbp + sf
obp = ob1 / float(ob2) 
print obp