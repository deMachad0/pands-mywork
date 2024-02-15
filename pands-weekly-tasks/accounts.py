# a program that reads 10 characteres account amount 
# and outputs only the last 4 digits
# Author: Andre Machado

print("$ Python accounts.py ")

# number will alocate the value of the user input
number = (input("Please enter an 10 digit account number: "))

# number[-4:] keeps the last 4 values 
# rjust(len(number), 'X') adds X in all numbers of the left
# len(number) return the length of the number
result = number[-4:].rjust(len(number), 'X')
print(result)
