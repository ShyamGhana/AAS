# SESSION 34 – GOOGLE (Teleoperation)

# Step 1: Import library
import pandas as pd

# Step 2: Simulated dataset (Teleop Keyboard Dataset)
# Represents keyboard inputs sent to robot

data = {
    "key_pressed": ["A"]  # User input
}

dataset = pd.DataFrame(data)

print("Using Dataset: Teleop Keyboard Dataset (ROS Teleop Simulation)")
print(dataset)

# Step 3: Extract key input
key = dataset["key_pressed"][0]

# Step 4: Map key to robot command
if key.upper() == "A":
    command = "Left Turn"
elif key.upper() == "D":
    command = "Right Turn"
elif key.upper() == "W":
    command = "Move Forward"
elif key.upper() == "S":
    command = "Move Backward"
else:
    command = "No Action"

# Step 5: Display results
print("\nKey Pressed:", key)
print("Robot Command:", command)

#OUTPUT

Key Pressed: A
Robot Command: Left Turn
