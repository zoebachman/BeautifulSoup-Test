from bs4 import BeautifulSoup

import urllib2

f = urllib2.urlopen("https://newyork.craigslist.org/search/zip")

soup = BeautifulSoup(f, 'html.parser')

# print soup.title.string

print soup.find(id ="titletextonly")

print soup.body.section.form 

myspans = soup.findAll('span', {"class": "titletextonly"}) 
# all span tags
for myspan in myspans:
	print myspan



