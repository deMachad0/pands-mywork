# User inputs a number positive and outputs the 
# sucessive values of the collatz calculation
# even number = divide by two
# odd number = multiply by three and add one
# the end value is one
# Author: Andre Machado

print(" Python collatz.py")


number = int(input("Please enter a positive integer: "))

numbers = []

# performs the while loop until the number becomes 1
while number != 1:
    numbers.append(number)
    # getting the even numbers 
    if number % 2 == 0:
       number = number // 2
    else:
    # getting the odd numbers
       number = number * 3 + 1  
for value in numbers:
   # using end=" " to print with space between the numbers
   print(value, end=" ")