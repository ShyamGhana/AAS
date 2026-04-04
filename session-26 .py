# SESSION 26 – WALMART (Predictive Maintenance)

# Step 1: Import libraries
import numpy as np
import pandas as pd

# Step 2: Simulated dataset (NASA Turbofan Engine Data)
# Typically includes sensor readings like temperature & vibration

data = {
    "Temperature": [80],
    "Vibration": [10]
}

dataset = pd.DataFrame(data)

print("Using Dataset: NASA Turbofan Engine (Simulated Sample)")
print(dataset)

# Step 3: Extract values
T = dataset["Temperature"][0]
V = dataset["Vibration"][0]

# Step 4: Compute Health Score
health = 100 - (0.4 * T + 1.1 * V)

# Step 5: Display results
print("\nTemperature (T):", T)
print("Vibration (V):", V)
print("Health Score:", health)

# Step 6: Maintenance Interpretation
if health > 70:
    status = "Good Condition"
elif health > 50:
    status = "Moderate Condition"
else:
    status = "Maintenance Required"

print("System Status:", status)

#OUTPUT

Temperature (T): 80
Vibration (V): 10
Health Score: 57.0
System Status: Moderate Condition
