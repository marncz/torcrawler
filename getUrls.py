import proxySettings
import urllib2
import dbConnect
import re
import time
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://zqktlwi4fecvo6ri.onion/wiki/Main_Page")
soup = BeautifulSoup(page.read())
soup.prettify()
date = time.strftime("%Y-%m-%d")
for anchor in soup.findAll('a', href=True):
	if anchor['href'].find(".onion/") != -1: # check if url contains .onion domain
		query = "INSERT INTO tc_urls (id,url,date_crawled,title) values ('','%s','%s','title')" % (anchor['href'],date)
		dbConnect.execute(query);

		url = anchor['href']
		m = re.search(r'(?<=\http://)(.*?)(?=\.onion)', url)
		if m:
			print "Url: %s Onion: %s" % (url,m.group(0))
			
