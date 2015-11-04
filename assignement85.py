fname = raw_input("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print ("File Not Found")
    exit()

count = 0
wrdlist = list()
    
for line in fhandle:
    if line.startswith("From "):
        wrdlist = line.split()
        print wrdlist[1]
        count += 1

print "There were %d line in the files with From as the first word" % count

