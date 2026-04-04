# SESSION 17 – NVIDIA (RRT)

# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Define goal position (x, y)
goal = np.array([2.0, 2.0])

# Step 3: Simulated new node (sampled point)
new_node = np.array([1.8, 1.9])

# Step 4: Define goal radius
goal_radius = 0.4

# Step 5: Compute distance between node and goal
distance = np.linalg.norm(new_node - goal)

# Step 6: Check goal connection
if distance <= goal_radius:
    result = "Goal Connected"
else:
    result = "Not Connected"

# Step 7: Display results
print("Goal Position:", tuple(goal))
print("New Node:", tuple(new_node))
print("Distance to Goal:", round(distance, 2))
print("Goal Radius:", goal_radius)
print("Result:", result)

# Step 8: Visualization (for understanding)
plt.figure()

# Plot goal
plt.scatter(goal[0], goal[1], label="Goal", marker='*')

# Plot new node
plt.scatter(new_node[0], new_node[1], label="New Node")

# Draw goal radius circle
circle = plt.Circle(goal, goal_radius, fill=False)
plt.gca().add_patch(circle)

plt.title("RRT Goal Connection Check")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

#OUTPUT

Goal Position: (np.float64(2.0), np.float64(2.0))
New Node: (np.float64(1.8), np.float64(1.9))
Distance to Goal: 0.22
Goal Radius: 0.4
Result: Goal Connected

plt.show()
