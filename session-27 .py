# SESSION 27 – AMAZON (Go-To-Goal Navigation)

# Step 1: Import libraries
import numpy as np
import pandas as pd

# Step 2: Simulated dataset (2D Navigation Dataset)
# Contains robot start and goal positions

data = {
    "start_x": [0],
    "start_y": [0],
    "goal_x": [6],
    "goal_y": [8]
}

dataset = pd.DataFrame(data)

print("Using Dataset: 2D Navigation Dataset (ROS2 Nav2 Simulation)")
print(dataset)

# Step 3: Extract values
x1 = dataset["start_x"][0]
y1 = dataset["start_y"][0]
x2 = dataset["goal_x"][0]
y2 = dataset["goal_y"][0]

# Step 4: Compute Euclidean distance
distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Step 5: Display results
print("\nStart Position:", (x1, y1))
print("Goal Position:", (x2, y2))
print("Distance to Goal:", distance, "m")

#OUTPUT

Start Position: (np.int64(0), np.int64(0))
Goal Position: (np.int64(6), np.int64(8))
Distance to Goal: 10.0 m
