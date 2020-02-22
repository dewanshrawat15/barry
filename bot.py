from selenium import webdriver
import csv
import time
import os
from os import system, name
from selenium.webdriver.common.keys import Keys

def init():
	global browser
	browser = webdriver.Chrome()
	browser.get("https://google.com")
	time.sleep(2)

def windows(links):
	counter = 0
	for i in links:
		browser.execute_script('''window.open(" ''' + i + '''", "_blank", "height=600,width=800,top=''' + str(counter) + ''', left=''' + str(counter) + '''");''')
		counter = counter + 20

def search(param):
	searchBar = browser.find_element_by_name('q')
	searchBar.send_keys(param)
	searchBar.send_keys(Keys.ENTER)
	time.sleep(2)
	searchResults = browser.find_elements_by_class_name('r')
	links = []
	for i in searchResults:
		try:
			tempLinkElem = i.find_element_by_tag_name('a')
		except:
			continue
		tempLink = tempLinkElem.get_attribute("href")
		links.append(tempLink)
	windows(links)

x = input("What would you like to search for? ")
init()
search(x)