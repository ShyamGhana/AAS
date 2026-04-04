# SESSION 23 – MICROSOFT (Feedback Control)

# Step 1: Import library
import numpy as np

# Step 2: Simulated dataset (PID Control Dataset)
# Represents sensor readings and desired setpoint

dataset = {
    "setpoint": 10,
    "actual_value": 7
}

print("Using Dataset: PID Control Dataset (Arduino PID Simulation)")

# Step 3: Extract values
setpoint = dataset["setpoint"]
actual = dataset["actual_value"]

# Step 4: Compute error
error = setpoint - actual

# Step 5: Display results
print("Setpoint:", setpoint)
print("Actual Value:", actual)
print("Control Error:", error)

#OUTPUT

Using Dataset: PID Control Dataset (Arduino PID Simulation)
Setpoint: 10
Actual Value: 7
Control Error: 3
