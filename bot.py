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

def search(param):
	searchBar = browser.find_element_by_name('q')
	searchBar.send_keys(param)
	searchBar.send_keys(Keys.ENTER)
	time.sleep(2)
	searchResults = browser.find_elements_by_class_name('r')
	print(type(searchResults[0]))
	print(len(searchResults))
	links = []
	for i in searchResults:
		tempLinkElem = i.find_element_by_tag_name('a')
		tempLink = tempLinkElem.get_attribute("href")
		links.append(tempLink)
	print(links)

x = input("What would you like to search for? ")
init()
search(x)