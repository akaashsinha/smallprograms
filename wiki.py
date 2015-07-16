# Scrapes the information from a random Wikipedia page
import requests
from bs4 import BeautifulSoup


r = requests.get("https://en.wikipedia.org/wiki/Special:Random")
soup = BeautifulSoup(r.content)


for link in soup.find_all('p'):
	print link.text
