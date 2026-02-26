# SESSION 7 – JPMORGAN (Optimization)
# Industry: AI Ops Optimization

# Step 1: Synthetic Optimization Dataset (sample values)
# (dataset included as instructed)
import numpy as np

x_values = np.linspace(-10, 10, 100)
y_values = (x_values - 3) ** 2   # Synthetic optimization function


# Step 2: Define optimization function
def optimization_function(x):
    return (x - 3) ** 2


# Step 3: Compute derivative
def derivative(x):
    return 2 * (x - 3)


# Step 4: Find minima
# Condition: derivative = 0
# Solve: 2(x - 3) = 0 → x = 3

min_x = 3
min_value = optimization_function(min_x)


# Step 5: Output results
print("Output: x =", min_x)
print("Industry: AI Ops Optimization")

# OUTPUT 
Output: x = 3
Industry: AI Ops Optimization

