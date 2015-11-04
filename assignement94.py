sndrdict = dict()
sndrnamecommon = None
sndrcountcommon = None

# ask for filename, if None then replace for default
fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fhandle = open(fname)
except:
    print "File not found!"
    exit()
    
# find the sender names and add them to the dictionary    
for adrline in fhandle :
    if adrline.startswith ("From "):
        sndrlist = adrline.split()
        sndrdict[sndrlist[1]] = sndrdict.get(sndrlist[1],0) + 1

# find the most common name. Keep in mind the tuple is separated by a comma, not a dot!
for sndrname,sndrcount in sndrdict.items() :
    if sndrcount is None or sndrcount > sndrcountcommon :
        sndrnamecommon = sndrname
        sndrcountcommon = sndrcount
    
print sndrnamecommon,sndrcountcommon


        
        
