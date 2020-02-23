from selenium import webdriver
import csv
import time
import os
from os import system, name
from selenium.webdriver.common.keys import Keys
import argparse


class Barry:
	def __init__(self):
		self.browser = webdriver.Chrome()

	def windows(self, links):
		counter = 0
		for i in links:
			self.browser.execute_script('''window.open(" ''' + i + '''", "_blank", "height=600,width=800,top=''' + str(counter) + ''', left=''' + str(counter) + '''");''')
			counter = counter + 20

	def googleSearch(self, param):
		self.browser.get("https://google.com")
		time.sleep(2)
		searchBar = self.browser.find_element_by_name('q')
		searchBar.send_keys(param)
		searchBar.send_keys(Keys.ENTER)
		time.sleep(2)
		searchResults = self.browser.find_elements_by_class_name('r')
		links = []
		for i in searchResults:
			try:
				tempLinkElem = i.find_element_by_tag_name('a')
			except:
				continue
			tempLink = tempLinkElem.get_attribute("href")
			links.append(tempLink)
		self.windows(links)

	def bingSearch(self, param):
		self.browser.get("https://bing.com")
		time.sleep(2)
		searchBar = self.browser.find_element_by_name('q')
		searchBar.send_keys(param)
		searchBar.send_keys(Keys.ENTER)
		time.sleep(2)
		searchResults = self.browser.find_elements_by_class_name('b_algo')
		links = []
		for i in searchResults:
			try:
				tempLinkElem = i.find_element_by_tag_name('a')
			except:
				continue
			if "http" in tempLinkElem.get_attribute('href'):
				links.append(tempLinkElem.get_attribute('href'))
		self.windows(links)

parser = argparse.ArgumentParser(description="Hey there, I'm Barry. A tool utility in the making of Jarvis.")
parser.add_argument("-p", "--param", help="Enter the search parameter")
parser.add_argument("-e", "--engine", help="Enter the preferred search engine. Default is Google.")
args = parser.parse_args()
ch = 'y'
used = False
while ch == 'y':
	if not args.param and args.engine is None:
		x = input("Enter your search query: ")
		Barry().googleSearch(x)
	if used:
		x = input("Enter a search query: ")
		Barry().googleSearch(x)
	else:
		if args.engine == 'google' and args.param:
			Barry().googleSearch(args.param)
		elif args.engine == 'bing' and args.param:
			Barry().bingSearch(args.param)
	used = True
	ch = input("Wanna continue ? ")