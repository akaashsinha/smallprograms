hr = input("How many homeruns did give up ")
bb = input("How many walks did he give ")
h = input("How many batters did he hit ")
k = input("How many strikeouts did he give ")
ip = input("How many innings did he pitch ")
batters = h + bb
fi = (13 * hr) + (3 * batters) - (2 * k)
fi2 = fi / float(ip)
fip = fi2 + 3.084
print fip
