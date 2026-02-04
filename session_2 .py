# SESSION 2 – AMAZON (Obstacle Detection)
# Dataset: Intel RealSense Depth Dataset

# Step 1: Import required libraries
import numpy as np
import subprocess
import os

# Step 2: Clone Intel RealSense repository (dataset source)
repo_url = "https://github.com/IntelRealSense/librealsense.git"
repo_name = "librealsense"

if not os.path.exists(repo_name):
    subprocess.run(["git", "clone", repo_url])

# Step 3: Read depth values (simulated depth frame for Colab execution)
# Note: RealSense cameras require hardware, so a sample depth array is used
depth_values = np.array([
    0.8, 0.6, 0.45, 0.7, 0.9
])

# Step 4: Initialize robot velocity
velocity = 1.0  # initial velocity (moving)

# Step 5: Apply threshold logic
distance = depth_values.min()

# Code Logic (as given in instructions)
if distance < 0.5:
    velocity = 0

# Step 6: Output result
if velocity == 0:
    print("Output: Robot Halted")
    print("Industry: Amazon Fulfillment Robots")
else:
    print("Output: Robot Moving")
    print("Industry: Amazon Fulfillment Robots")
