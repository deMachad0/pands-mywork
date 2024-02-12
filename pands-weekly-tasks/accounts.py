# a program that reads 10 characteres account amount 
# and outputs only the last 4 digits
# Author: Andre Machado

print("$ Python accounts.py ")
number = (input("Please enter an 10 digit account number: "))

result = number[-4:].rjust(len(number), 'X')
print(result)
