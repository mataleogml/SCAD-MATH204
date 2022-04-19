#   SCAD Spring 2022 - Math204-N01 - Professor Juras
#   Week 1 - Python Basics: Problem 1

# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

count = 0
s = input("Enter a string: ")
for n in s:
    if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
        count += 1
        print(n)
print("Number of vowels:" + str(count))