# prompt the user and read in two money amounts
# author name: Andre Machado
# print in human readable format with euro sign and decimal

print("$ python bank.py ")

# amount1 and amount2 will allocate the value of the user input
amount1 = int( input("Enter the amount1(in cent): "))
amount2 = int( input("Enter the amount2(in cent): "))

# division to transform the value in cents
result = (amount1 / 100 + amount2 / 100)

# \N{euro sign} A character can be assigned to 
# a string using its official Unicode name
print(f"The sum of these is: \N{euro sign}{result}")