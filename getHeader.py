import urllib2
import proxySettings
import dbConnect

def getHeader(url):
	page = urllib2.urlopen(url)
	print page.info() # get http header response

getHeader("http://zqktlwi4fecvo6ri.onion/wiki/Main_Page")


dbConnect.execute("show tables");
