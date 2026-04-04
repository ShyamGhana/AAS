# SESSION 16 – AMAZON (Path Planning)

# Step 1: Import libraries
import matplotlib.pyplot as plt

# Step 2: Define path costs
path_A_cost = 6
path_B_cost = 4

# Step 3: Compare paths (Greedy Decision Rule)
if path_A_cost < path_B_cost:
    selected_path = "Path A"
else:
    selected_path = "Path B"

# Step 4: Display results
print("Path A Cost:", path_A_cost)
print("Path B Cost:", path_B_cost)
print("Selected Path:", selected_path)

# Step 5: Visualization (for understanding)
paths = ['Path A', 'Path B']
costs = [path_A_cost, path_B_cost]

plt.bar(paths, costs)
plt.title("Path Cost Comparison")
plt.ylabel("Cost")
plt.show()

#OUTPUT

Path A Cost: 6
Path B Cost: 4
Selected Path: Path B
