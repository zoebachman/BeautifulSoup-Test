from bs4 import BeautifulSoup
import urllib2

website = 'http://newyork.craigslist.org/search/zip'

for i in range(5):
	if i > 0:
		website = 'http://newyork.craigslist.org/search/zip?s=' + str(i*100)

	f = urllib2.urlopen(website)

	soup = BeautifulSoup(f,'html.parser')
	newSoup = soup.body.find(id="searchform")
	myspans = []
	myspans = newSoup.find_all("span", {"id" : "titletextonly" })
	for myspan in myspans:
		print myspan.text


