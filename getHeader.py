import urllib2
import proxySettings
import dbConnect
import time

def getHeader(url):
	page = urllib2.urlopen(url)
	return page.info() # get http header response

url = "http://zqktlwi4fecvo6ri.onion/wiki/Main_Page"
header = getHeader(url)
date = time.strftime("%Y-%m-%d")
print header

query = "INSERT INTO tc_headers (url,header,date) values ('%s','%s','%s')" % (url,header,date)
dbConnect.execute(query);
	
