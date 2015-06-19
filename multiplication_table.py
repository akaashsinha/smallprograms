def spaces(z):
	if z < 10:
		return 3
	elif z < 100:
		return 2
	else:
		return 1

def multiplicaton_table(x):	
	if x < 0:
		print "You can only enter positive numbers"

	if x == 0:
		print "You entered zero, please enter another number"

	if x > 16:
		print "You might need to expand you window!"

	for j in range(1,int(x) + 1):
		for z in range(1,int(x) + 1):
			print str(j * z) + " "  * spaces(j * z),
		print " "
		
parameter = input("Enter the the max: ")

multiplicaton_table(parameter)