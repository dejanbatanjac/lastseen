import sys
import time
from lxml import html
import requests

__VERSION__ = '0.0.1'

id = 5884955
global url 
url = "https://stackoverflow.com/users/" + str(id)
# we will seek this html
# last_seen = '<div class="grid--cell fl1">Last seen <span title="2019-01-31 10:29:21Z" class="relativetime">7 mins ago</span></div>'

# empty tuple


def getpage(url):
	'''  returns tuple in the format like this:
	    ("2019-01-31 11:33:55Z", "4 mins ago")
	'''	
	try:
		page = requests.get(url)
	except Exception as e:
		return ("", "")
	else:
		tree = html.fromstring(page.content)
		time = tree.xpath('//span[@class="relativetime"]/@title')
		text = tree.xpath('//span[@class="relativetime"]/text()')
	finally:
		return (time[0], text[0])
	
	



def main():

	last =("","")

	while True:
		t = getpage(url)

		# on error exit the program
		if(t[0]==""):
			sys.exit(1)
		
		if (t[0]!=last[0]):
			f = open(str(id), "a")
			f.writelines(t[0] +": "+ t[1] + "\n") 
			f.close()
			
		
		last = t
		time.sleep(60) #on 60 seconds


if __name__ == '__main__':
    main()