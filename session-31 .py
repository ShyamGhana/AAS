# SESSION 31 – NVIDIA (System Integration)

# Step 1: Import library
import pandas as pd

# Step 2: Simulated dataset (ROS2 Full Stack Logs)
# Represents outputs from perception, planning, control modules

data = {
    "perception_status": ["Object Detected"],
    "planning_status": ["Path Planned"],
    "control_status": ["Motion Executed"]
}

dataset = pd.DataFrame(data)

print("Using Dataset: ROS2 Full Stack Logs (Simulation)")
print(dataset)

# Step 3: Extract module outputs
perception = dataset["perception_status"][0]
planning = dataset["planning_status"][0]
control = dataset["control_status"][0]

# Step 4: System integration logic
if perception and planning and control:
    result = "Autonomous Execution Successful"
else:
    result = "Execution Failed"

# Step 5: Display results
print("\nPerception:", perception)
print("Planning:", planning)
print("Control:", control)
print("Final Output:", result)

#OUTPUT

Perception: Object Detected
Planning: Path Planned
Control: Motion Executed
Final Output: Autonomous Execution Successful

