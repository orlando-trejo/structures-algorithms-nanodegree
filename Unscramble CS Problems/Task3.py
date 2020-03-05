"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
# Get list of all numbers called by people in Bangalore
num_bang = []
for row in calls:
    num1 = row[0]
    if ("(080)" in num1):
        num_bang.append(row[1])

# Get the codes from all the numbers
codes = []
for number in num_bang:
    if ("(0" in number):
        pos = number.index(')')
        codes.append(int(number[1:pos]))
    elif ("140" == number[0:3]):
        codes.append(140)
    else:
        codes.append(int(number[0:4]))

# Find and sort unique codes
uniq_codes = list(set(codes))
uniq_codes.sort()
# Print statements
print("The numbers called by people in Bangalore have codes:")
for code in uniq_codes:
    print(code)

# Part B
perc = codes.count(80) / len(codes) * 100
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(perc,2)))
