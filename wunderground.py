# This program gets the conditions and the temperature of Athens Georgia. My first try with an API. I used the underground API.

import requests
# supply your own api key

url = "http://api.wunderground.com/api/api_key_goes_here/forecast/q/GA/Athens.json"
r = requests.get(url)

info = r.json()

choice = input("Do you want your temperature in Fahrenheit or Celsius? Press 1 for Fahrenheit, press any other key for Celsius ")



print ""
for day in info['forecast']['simpleforecast']['forecastday']:
	print day['date']['weekday'], day['date']['day'], day['date']['monthname'] + ":"
	print "Conditions:", day['conditions']
	if choice == 1:
		print "Today's high is: ", day['high']['fahrenheit'], "Today's low is:", day['low']['fahrenheit'] + "\n"
	else:
		print "Today's high is: ", day['high']['celsius'], "Today's low is:", day['low']['celsius'] + "\n"

print "Have a nice day!"




