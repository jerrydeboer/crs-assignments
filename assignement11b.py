# assignment 11 with list comprehension
# ch 11, comprehension, ch 7 read() of python for informatics

# open file with name: regex_sum_42.txt -> open('regex_sum_42.txt')
# read the file in memory -> open('regex_sum_42.txt').read()
# find & extract numbersstrings from above file -> re.findall('([0-9]+)', open('regex_sum_42.txt').read())
# itterate thru numbers in temporary list created above -> for numstr in re.findall('([0-9]+)', open('regex_sum_42.txt').read())
# convert each numberstring in integer, so a new temporary list but now with integers -> int(numstr) for numstr in re.findall('([0-9]+)', open('regex_sum_42.txt').read()))
# summarize  the integer list created above -> sum( int(numstr) for numstr in re.findall('([0-9]+)', open('regex_sum_42.txt').read()))
# print the sum of the list -> print sum( int(numstr) for numstr in re.findall('([0-9]+)', open('regex_sum_42.txt').read()))

import re
print sum( int(numstr) for numstr in re.findall('([0-9]+)', open('regex_sum_42.txt').read()))
