#variable declaration
largest = None
smallest = None

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
    # check for smallest number    
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num
    # check for largest number
    if largest is None :
        largest = num
    elif num > largest :
        largest = num
        
print "smallest: ", smallest
print "largest: ", largest
    
