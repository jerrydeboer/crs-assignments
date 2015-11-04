# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# declare variables
countline = 0
total = 0

# Query for filename
fname = "mbox-short.txt"
# fname = raw_input("Enter file name: ")
try :
    fhandle = open(fname)
except :
    print "Unknown Filename"
    exit()
    
for line in fhandle :
    if not line.startswith("X-DSPAM-Confidence:") : continue
    chrpos = line.find(":")
    chrnum = line[chrpos+1:].strip()
    total = total + float(chrnum)
    countline = countline + 1
print "Average spam confidence: ", total/countline


    
# Read file
# fcontent = fhandle.read()
# fcontent = fcontent.strip()
# print fcontent.upper()

