# SESSION 24 – NVIDIA (C-Space / Configuration Space)

# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Simulated dataset (Motion Planning Map)
# 0 = free space, 1 = obstacle
map_data = np.zeros((10, 10))

# Add an obstacle in center
map_data[4:6, 4:6] = 1

print("Using Dataset: Motion Planning Map (Grid Simulation)")

# Step 3: Robot radius (inflation value)
robot_radius = 0.6

# Step 4: Inflate obstacles (simple approximation)
inflated_map = map_data.copy()

for i in range(map_data.shape[0]):
    for j in range(map_data.shape[1]):
        if map_data[i, j] == 1:
            # Inflate surrounding cells
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < 10 and 0 <= y < 10:
                        inflated_map[x, y] = 1

# Step 5: Display maps
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(map_data)
plt.title("Original Map")

plt.subplot(1,2,2)
plt.imshow(inflated_map)
plt.title("C-Space (Inflated Obstacles)")

plt.show()

# Step 6: Output
print("Robot Radius:", robot_radius, "m")
print("Result: Collision-Free Space Generated")

#OUTPUT

Robot Radius: 0.6 m
Result: Collision-Free Space Generated
