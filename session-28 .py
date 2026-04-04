# SESSION 28 – TESLA (Obstacle Avoidance)

# Step 1: Import libraries
import pandas as pd

# Step 2: Simulated dataset (CARLA Simulator Sensor Data)
# Represents distance measured by proximity sensors

data = {
    "obstacle_distance": [0.25]  # meters
}

dataset = pd.DataFrame(data)

print("Using Dataset: CARLA Simulator (Obstacle Sensor Data)")
print(dataset)

# Step 3: Extract value
distance = dataset["obstacle_distance"][0]

# Step 4: Define safety threshold
threshold = 0.5  # meters

# Step 5: Reactive control rule
if distance < threshold:
    action = "Turn Right"
else:
    action = "Move Forward"

# Step 6: Display results
print("\nObstacle Distance:", distance, "m")
print("Threshold:", threshold, "m")
print("Action:", action)

#OUTPUT

Obstacle Distance: 0.25 m
Threshold: 0.5 m
Action: Turn Right
