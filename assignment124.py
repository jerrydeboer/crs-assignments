# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
c_input = raw_input('Enter count: ')
p_input = raw_input('Enter position: ')

if len(url) < 1 : url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Guang.html'
if len (c_input) < 1 :
    count = 7
else :
    count = int(c_input)
if len (p_input) < 1 :
    pos = 18
else :
    pos = int(p_input)

c = 0
while c < count :
    c += 1
    try :
        html = urllib.urlopen(url).read()
    except :
        print 'Not a valid url'
        exit()
    soup = BeautifulSoup(html)
    tags = soup('a')
    maxlinks = len(tags)
    if pos <= maxlinks :
        url = tags[pos-1].get('href', None)
        print 'Retrieving: ', url
        continue
    else :
        print 'url position exceeds number of urls on page'
print 'Last Url:   ', url
print 'Last name: '.join(re.findall('known_by_(.+).html', url))
