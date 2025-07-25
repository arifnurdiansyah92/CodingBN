import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare your data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 2. Create the plot piece by piece
plt.plot(x, y) # Add the line
plt.title("My First Masterpiece") # Add the title
plt.xlabel("X-Axis") # Add the x-label
plt.ylabel("Y-Axis") # Add the y-label

# 3. Show your art to the world
plt.show()
