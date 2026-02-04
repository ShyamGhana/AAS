# SESSION 3 – TESLA (Sensor Selection)
# Dataset: KITTI Vision Benchmark

# Step 1: Import required libraries
import numpy as np
import requests

# Step 2: Dataset reference (KITTI Vision Benchmark)
kitti_dataset_url = "http://www.cvlibs.net/datasets/kitti/"

# Step 3: Sensor range metadata (from KITTI sensor specifications)
# Values are standard sensor ranges used in autonomous vehicles

sensor_metadata = {
    "Camera": 50,    # range in meters
    "Radar": 100,    # range in meters
    "LiDAR": 200     # range in meters
}

# Step 4: Compare sensor ranges
selected_sensor = max(sensor_metadata, key=sensor_metadata.get)

# Step 5: Output result (as per instructions)
if selected_sensor == "LiDAR":
    print("Output: LiDAR Selected")
    print("Industry: Tesla Autopilot")
else:
    print("Output:", selected_sensor, "Selected")
    print("Industry: Tesla Autopilot")
