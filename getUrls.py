import proxySettings
import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://zqktlwi4fecvo6ri.onion/wiki/Main_Page")
soup = BeautifulSoup(page.read())
soup.prettify()
for anchor in soup.findAll('a', href=True):
	if anchor['href'].find(".onion/") != -1: # check if url contains .onion domain
		print anchor['href']
