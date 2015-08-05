__author__ = 'akaash'
# Might have to stop the page for this program to work
# For some reason Fangraphs takes too long to load naturally during this program
# Might extend this so it searches Baseball-Reference.com or maybe even both at the same time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

player_name = raw_input("Enter the player you want to search ")


browser = webdriver.Firefox()

browser.get("http://www.fangraphs.com")
form = browser.find_element_by_id("psbox")
form.send_keys(player_name)
form.send_keys(Keys.RETURN)
