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
TASK 4:
The telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Create function that gets list of incoming or answering number
def get_numbers(list, column):
    ''' Input: list and column number
        Output: list
    '''
    return [list[i][column] for i in range(len(list))]

# Create sets
incoming_calls = set(get_numbers(calls, 0))
receiving_calls = set(get_numbers(calls, 1))
incoming_texts = set(get_numbers(texts, 0))
receiving_texts = set(get_numbers(texts, 1))

# Find potential telemarketers
potential_numbers = incoming_calls - receiving_calls - incoming_texts - receiving_texts
potential_numbers = list(potential_numbers)
potential_numbers.sort()

# Print statements
print("These numbers could be telemarketers: ")
for number in potential_numbers:
    print(number)
