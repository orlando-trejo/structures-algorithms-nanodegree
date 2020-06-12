# @Author: otrejo
# @Date:   2020-05-20T22:24:35-04:00
# @Last modified by:   otrejo
# @Last modified time: 2020-06-12T12:39:13-04:00

import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    lookup_table = [0] * (knapsack_max_weight + 1)

    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity],
                                             lookup_table[capacity-item.weight] + item.value)

    return lookup_table[-1]



tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == max_value(**test['input'])

# Longest Common Subsequence
import numpy as np

def lcs(string_a, string_b):
    len_a = len(string_a)+1
    len_b = len(string_b)+1

    matrix = np.zeros((len_b, len_a))

    for i in range(len_b-1):
        for j in range(len_a-1):
            #print(string_a[j], string_b[i])
            if string_a[j] == string_b[i]:
                matrix[i+1, j+1] = matrix[i, j] + 1
            if string_a[j] != string_b[i]:
                matrix[i+1, j+1] = max(matrix[i, j+1], matrix[i+1, j])


    return (int(np.max(matrix)))

## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')
# Complexity is O(N^2) due to two nested loops

# Longest Palindromic Subsequence
def lps(input_string):
    len_string = len(input_string)
    matrix = np.zeros((len_string, len_string))
    np.fill_diagonal(matrix, 1)

    for j in range(0, len_string):
        for i in reversed(range(0, j)):
            if input_string[i] == input_string[j]:
                matrix[i,j] = matrix[i+1, j-1] + 2
            if input_string[i] != input_string[j]:
                matrix[i,j] = max(matrix[i+1, j], matrix[i, j-1])


    print(matrix)
    return (int(np.max(matrix)))

def test_function(text_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)

string = 'BANANA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

# The Coin Change Problem
def coin_change(coins, amount):
    # Store coins with amounts
    memo = {}

    # Recursive function to determine change
    def return_change(remaining):
        # Base cases
        if remaining < 0:
            return float('inf')
        if remaining == 0:
            return 0

        # Cehck if previously calculated
        if remaining not in memo:
            memo[remaining] = min(return_change(remaining-c)+1 for c in coins)

        return memo[remaining]

    res = return_change(amount)

    return -1 if res == float('inf') else res

def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)


# Stock Prices
def max_returns(prices):
    """
    Calculate maxiumum possible return

    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0

    if len(prices) < 2:
        return

    for i in range(1, len(prices)):
        if prices[i] < prices[current_min_price_index]:
            current_min_price_index = i

        if prices[max_price_index] - prices[min_price_index] < prices[i] - prices[current_min_price_index]:
            max_price_index = i
            min_price_index = current_min_price_index

    max_profit = prices[max_price_index] - prices[min_price_index]

    return max_profit

# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass Profits")
    else:
        print("Fail")


prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)
