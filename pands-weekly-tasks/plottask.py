#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range 0 to 10, 
#on the one set of axes.
#Author: Andre Machado

import numpy as np
import matplotlib.pyplot as plt

# random numbers will be the same each time
np.random.seed(1)
# Generating 1000 random values using normal distribution
normal_data = np.random.normal(5, 2, 1000)
# Plotting histogram
plt.hist(normal_data, color="blue", edgecolor='white')
plt.title("Histogram of normal distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")


# Creating the function h(x) = X^3
x = np.array(range(0,11))
h = x ** 3

# Plotting the function
plt.plot(x, h, color='red', label="Plot h(x) = x^3")
plt.xlabel("x")
plt.ylabel("h(x)")

# Displaying legends
plt.legend()
plt.show()
