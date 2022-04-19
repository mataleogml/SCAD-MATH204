#   SCAD Spring 2022 - Math204-N01 - Professor Juras
#   Week 1 - Python Basics: Exercise 2

#   Assume s is a string of lower case characters.
#   Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your
#   program should print
#   Number of times bob occurs is: 2

count = 0
s = input("Enter a string: ")
for n in range(len(s)):
    if s[n:n+3] == "bob":
        count += 1
print("Number of times bob occurs is:" + str(count))