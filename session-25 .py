# SESSION 25 – GOOGLE (Artificial Potential Fields)

# Step 1: Import library
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Simulated dataset (Artificial Potential Field Data)
# Represents forces acting on robot

dataset = {
    "attractive_force": 12,
    "repulsive_force": 5
}

print("Using Dataset: Artificial Potential Field Data (PythonRobotics Simulation)")

# Step 3: Extract values
attractive = dataset["attractive_force"]
repulsive = dataset["repulsive_force"]

# Step 4: Compute net force
net_force = attractive - repulsive

# Step 5: Display results
print("Attractive Force:", attractive)
print("Repulsive Force:", repulsive)
print("Net Force:", net_force)

# Step 6: Visualization (for understanding)
labels = ['Attractive', 'Repulsive', 'Net']
values = [attractive, repulsive, net_force]

plt.bar(labels, values)
plt.title("Artificial Potential Field Forces")
plt.ylabel("Force Value")
plt.show()

#OUTPUT

Using Dataset: Artificial Potential Field Data (PythonRobotics Simulation)
Attractive Force: 12
Repulsive Force: 5
Net Force: 7
