# SESSION 30 – GOOGLE (Wall Following)

# Step 1: Import library
import pandas as pd

# Step 2: Simulated dataset (Robot Wall Following Dataset)
# Represents distance readings from wall sensors

data = {
    "desired_distance": [0.5],  # meters
    "actual_distance": [0.2]    # meters
}

dataset = pd.DataFrame(data)

print("Using Dataset: Robot Wall Following Dataset (PythonRobotics Simulation)")
print(dataset)

# Step 3: Extract values
desired = dataset["desired_distance"][0]
actual = dataset["actual_distance"][0]

# Step 4: Compute error
error = desired - actual

# Step 5: Control logic
if actual < desired:
    action = "Move Away from Wall"
elif actual > desired:
    action = "Move Closer to Wall"
else:
    action = "Maintain Distance"

# Step 6: Display results
print("\nDesired Distance:", desired, "m")
print("Actual Distance:", actual, "m")
print("Error:", error)
print("Action:", action)

#OUTPUT

Desired Distance: 0.5 m
Actual Distance: 0.2 m
Error: 0.3
Action: Move Away from Wall
