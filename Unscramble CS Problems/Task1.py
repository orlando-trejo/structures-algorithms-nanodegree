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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create function that gets list of incoming or answering number
def get_numbers(list, column):
    ''' Input: list and column number
        Output: list
    '''
    return [list[i][column] for i in range(len(list))]

# Combine all the numbers
total_list = get_numbers(texts, 0) + get_numbers(texts, 1) + \
             get_numbers(calls, 0) + get_numbers(calls, 1)

# Count unique numbers
len_num = len(set(total_list))

# Print statement
print("There are {} different telephone numbers in the records.".format(len_num))
