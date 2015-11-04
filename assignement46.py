def computepay(h,r):
    if hrs <= 40:
        pay = hrs*rate
        return pay
    else:
        pay = (40*rate)+ (hrs-40)*1.5*rate
        return pay

try:
    inp = raw_input("Enter Hours: ")
    hrs = float(inp)
except:
    print "Please enter a numerical value"
    quit()

try:
    inp = raw_input("Enter Rate: ")
    rate = float(inp)
except:
    print "Please enter a numerical value"
    quit()    
    


p = computepay(hrs,rate)
print "Pay",p
