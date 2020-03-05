"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# Create function that gets list of incoming or answering number
def get_numbers(list, column):
    ''' Input: list and column number
        Output: list
    '''
    return [list[i][column] for i in range(len(list))]

# Combine all unique numbers used in calls
total_set = set(get_numbers(calls, 0) + get_numbers(calls, 1))

# Initialize dictionary
call_dict = {}
for number in total_set:
    call_dict[number] = 0

# Add call durations
for row in calls:
    num1 = row[0]
    num2 = row[1]
    duration = row[3]
    call_dict[num1] = call_dict[num1] + int(duration)
    call_dict[num2] = call_dict[num2] + int(duration)

# Get number with longest durations
num_long = max(call_dict, key=call_dict.get)

# Print statement
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(num_long, call_dict[num_long]))
