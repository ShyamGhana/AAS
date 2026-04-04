# SESSION 20 – TESLA (Navigation)

# Step 1: Import library
import numpy as np

# Step 2: Define distance to goal
distance_to_goal = 0.15  # meters

# Step 3: Define threshold
threshold = 0.2  # meters (goal radius)

# Step 4: Goal checking condition
if distance_to_goal < threshold:
    result = "Goal Reached"
else:
    result = "Goal Not Reached"

# Step 5: Display results
print("Distance to Goal:", distance_to_goal, "m")
print("Threshold:", threshold, "m")
print("Result:", result)

#OUTPUT

Distance to Goal: 0.15 m
Threshold: 0.2 m
Result: Goal Reached
