# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
# reuse of framework of example urllink.py as stated in the assignement

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
# if len(url) < 1 : url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html'
try :
    html = urllib.urlopen(url).read()
except :
    print 'Not a valid url'
    exit()

soup = BeautifulSoup(html)

# Retrieve all of the span tags
summarize = 0
tags = soup('span')
for tag in tags:
# content of span tag stored on index 0
    summarize += int(tag.contents[0])
print summarize
