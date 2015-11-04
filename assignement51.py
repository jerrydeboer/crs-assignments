#variable declaration
largest = None
smallest = None
total = 0
count = 0

while True:
    inp = raw_input("enter a number: ")
    
    # check for exit command
    if inp == "done" : break
    #catch illegal input
    try:
        num = float(inp)
    except:
        print "invalid input"
        continue
    total = total + num
    count = count + 1
    
print "number", num, " count", count, " total", total, " avarage", total/count
    
