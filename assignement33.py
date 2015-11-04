
inp = raw_input("Enter Score: ")

try:
    score = float(inp)
except:
    print "enter a numerical value"
    quit()

if score > 1.0:
    print "enter score between 0.0 and 1.0"
    quit()
elif score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
else:
    grade = "F"
    
print "Your grade is: ",grade
