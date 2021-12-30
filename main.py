########################################################################################################################
# numbers = [9, 8, 7]
# new_numbers = [n + 1 for n in numbers]
# new_numbers = [n - 1 for n in numbers]
# new_numbers = [n + 1 for n in numbers]
# new_plus_numbers = [n + 1 for n in numbers]
# new_multi_numbers = [n * 1 for n in numbers]
# new_multiple_numbers = [n - 1 for n in numbers]
# new_multi_numbers = [n * 1.1 for n in numbers]
# new_mod_numbers = [n % 1.1 for n in numbers]
# name = "Benjamin"
# letter_list = [letter for letter in name]
# new_range = [letter * 2 for letter in range(0, 5)]
# new_range = [letter * 2 for letter in range(0, 5)]
# names = ['Jon', 'Bill', 'Maria', 'Jenny', 'Jack', "Mark", "Amber", "Todd", "Anita", "Sandy"]
# new_four_names = [name for name in names if len(name) < 5]
# new_four_names = [name for name in names if len(name) < 4]
# new_capital_names = [name.upper() for name in names]

########################################################################################################################
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain
# every number in the list numbers but each number should be squared.

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
# # squared_numbers = [sqr_number * sqr_number for sqr_number in numbers]
# squared_numbers = [sqr_number**2 for sqr_number in numbers]
#
#
# #Write your code 👆 above:
#
# print(squared_numbers)

########################################################################################################################
# You are going to write a List Comprehension to create a new list called result. This new list should only contain the
# even numbers from the list numbers.

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
# result = [num for num in numbers if num % 2 == 0]
#
# #Write your code 👆 above:
#
# print(result)

########################################################################################################################
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

import pandas as pd

with open("file1.txt") as f:
    file1Data = [num.strip('\n') for num in f.readlines()]
# print(file1Data)

with open("file2.txt") as f:
    file2Data = [num.strip('\n') for num in f.readlines()]
# print(file2Data)

result = [int(num2) for num2 in file2Data if num2 in file1Data]

# Write your code above 👆

print(result)
