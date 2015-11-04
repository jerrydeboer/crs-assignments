# assignement 11 - regex
import re

numberlst = list()
n = 0
cnt = 0

fname = raw_input('Eneter filename: ')
if len(fname)<1 : fname = 'regex_sum_42.txt'
try:
    fhandle = open(fname)
except:
    print 'This is not a valid filename'
    exit()

for line in fhandle :
    numberstr = re.findall('([0-9]+)', line)
    if len(numberstr) == 0 : continue
    for  str in numberstr :
        n += int(str)
        cnt += 1
#        numberlst.append(n)
# print n, cnt
print n
