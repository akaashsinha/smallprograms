__author__ = 'akaash'
from selenium import webdriver

username = raw_input("Insert your reddit username ")
password = raw_input("Insert your reddit password ")
browser = webdriver.Firefox()

browser.get("https://www.reddit.com")
form = browser.find_element_by_name("user")
passwd = browser.find_element_by_name("passwd")
button = browser.find_element_by_class_name("btn")
form.send_keys(username)
passwd.send_keys(password)
button.click()
