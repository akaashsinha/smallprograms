from fractions import *

# raw_input("Do you want Fahereinheit or Celsius ")
answer = input("Do you want fahrenheit or celsius ")
if answer == 1:
	# fahrenheit to celsius
	c = input("Put the degrees Fahereinheit you want in Celsius  ")
	output_c =  0.55 * (c - 32)
	print output_c
	
	#celsius to fahrenehit

else:
	f = input("Put the degrees Celsius you want in Fahereinheit ")
	output_f = (1.80 * f) + 32
	print output_f
	#answer ==  "celsius" or answer == "c" or answer == "Celsius" or answer == "c" or answer == "c":