fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print("file not found")
    exit()

wrdlst = list()
newlst = list()

for line in fhandle:
    words = line.split()
    for word in words:
        wrdlst.append(word)

        
for i in range (len(wrdlst)):
    for c in range (len(newlst)):
        if wrdlst[i] == newlst[c]:
            break
        else:
            continue
    else:
        newlst.append(wrdlst[i])

newlst.sort()
print newlst
