hr = input("How many homeruns did give up ")
bb = input("How many walks did he give ")
k = input("How many strikeouts did he give ")
ip = input("How many innings did he pitch ")
fi = (13 * hr) + (3 * bb) - (2 * k) 
fi2 = fi / float(ip)
fip = fi2 + 3.10	
print fip