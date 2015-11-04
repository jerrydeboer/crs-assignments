# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use # the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt


# Query for filename
fname = raw_input("Enter file name: ")
try :
    fhandle = open(fname)
except :
    print "Unknown Filename"
    exit()
    
# Read file
fcontent = fhandle.read()
fcontent = fcontent.strip()
print fcontent.upper()

