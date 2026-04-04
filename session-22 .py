# SESSION 22 – AMAZON (Kinematics - Differential Drive)

# Step 1: Import library
import numpy as np

# Step 2: Simulated dataset (ROS2 Control style)
# Dataset contains wheel velocities from robot sensors

dataset = {
    "left_wheel_velocity": 3,
    "right_wheel_velocity": 3
}

print("Using Dataset: Differential Drive Dataset (ROS2 Control Simulation)")

# Step 3: Extract values
left_speed = dataset["left_wheel_velocity"]
right_speed = dataset["right_wheel_velocity"]

# Step 4: Determine motion type
if left_speed == right_speed:
    motion = "Straight Line Motion"
elif left_speed > right_speed:
    motion = "Turning Right"
else:
    motion = "Turning Left"

# Step 5: Display results
print("Left Wheel Speed:", left_speed)
print("Right Wheel Speed:", right_speed)
print("Motion Type:", motion)

#OUTPUT

Using Dataset: Differential Drive Dataset (ROS2 Control Simulation)
Left Wheel Speed: 3
Right Wheel Speed: 3
Motion Type: Straight Line Motion
