# SESSION 35 – APPLE (Localization)

# Step 1: Import library
import pandas as pd

# Step 2: Simulated dataset (AMCL Localization Data)
# Represents estimated vs ground-truth error

data = {
    "pose_error": [0.08]  # meters
}

dataset = pd.DataFrame(data)

print("Using Dataset: AMCL Localization Dataset (ROS Navigation Simulation)")
print(dataset)

# Step 3: Extract value
pose_error = dataset["pose_error"][0]

# Step 4: Define accuracy threshold
threshold = 0.1  # meters

# Step 5: Evaluate localization accuracy
if pose_error < threshold:
    result = "Accurate Localization"
else:
    result = "Localization Error Too High"

# Step 6: Display results
print("\nPose Error:", pose_error, "m")
print("Threshold:", threshold, "m")
print("Result:", result)

#OUTPUT

Pose Error: 0.08 m
Threshold: 0.1 m
Result: Accurate Localization
