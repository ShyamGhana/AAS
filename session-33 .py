# SESSION 33 – AMAZON (Wander Bot / Random Walk)

# Step 1: Import libraries
import numpy as np
import pandas as pd

# Step 2: Simulated dataset (Random Walk Dataset)
# Represents robot heading and random turn angles

data = {
    "current_direction": [0],   # degrees (initial heading)
    "random_angle": [90]        # degrees (turn)
}

dataset = pd.DataFrame(data)

print("Using Dataset: Random Walk Dataset (Nav2 Simulation)")
print(dataset)

# Step 3: Extract values
current_direction = dataset["current_direction"][0]
random_angle = dataset["random_angle"][0]

# Step 4: Update direction
new_direction = (current_direction + random_angle) % 360

# Step 5: Display results
print("\nCurrent Direction:", current_direction, "°")
print("Random Angle:", random_angle, "°")
print("New Direction:", new_direction, "°")

print("Output: Direction Updated")

#OUTPUT

Current Direction: 0 °
Random Angle: 90 °
New Direction: 90 °
Output: Direction Updated
