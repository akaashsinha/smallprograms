ubb = input("Insert how many non-intentional walks did he have? ")
hbp = input("Insert how many times he got hit by a pitch? ")
fb = input("Insert how many singles did he have? ")
#rboe = input("Insert how many times did he reach on an error? ")
sb = input("Insert how many doubles did he have? ")
tb = input("Insert how many triples did he have? ")
hr = input("Insert how many home runs did he have? ")
ab = input("Insert how many at bats did he have? ")
bb = input("Insert how many walks did he have? ")
ibb = input("Insert how many intentional walks did he have? ")
sf = input("Insert how many sac flies did he have? ")

ubb1 = (0.691 * ubb)
hbp1 = (0.722 * hbp)
fb1 = (0.884 * fb)
sb1 = (1.257 * sb)
tb1 = (1.593 * tb)
hr1 = (2.058 * hr)

woba1 = (ubb * 0.691) + (hbp * 0.722) + (fb * 0.884) +  (sb * 1.257) + (tb * 1.593) + (hr * 2.058) 
woba = woba1 / (ab + bb - ibb + sf + hbp)
print woba

