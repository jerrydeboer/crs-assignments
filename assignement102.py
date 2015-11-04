# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# 
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = raw_input("Enter file name: ")
if len(fname)<1 : fname = "mbox-short.txt"
try:
    fhandle = open(fname)
except:
    print "This is not a valid file name"
    exit()

# select From line, split into words and split the 5th word at the colon, count hours in dictionary
sndrdict = dict()
for sndrline in fhandle :
    if sndrline.startswith("From "):
        sndrlist = sndrline.split()
        colonpos = sndrlist[5].find(":")
        hour = sndrlist[5][:colonpos]
        sndrdict[hour] = sndrdict.get(hour,0)+1

# convert dict in list
srtlst = list()
for hr,c in sndrdict.items() :
    srtlst.append ((hr,c))

# sort list
srtlst.sort()
for hr,c in srtlst :
    print hr,c
