# SESSION 4 – APPLE (Motor Control)
# Dataset: NASA Robot Motor Dataset

# Step 1: Import required libraries
import pandas as pd
import numpy as np
import requests

# Step 2: Dataset reference (NASA Robot Motor Dataset)
nasa_dataset_url = "https://data.nasa.gov/Engineering/Robot-Motor-Data/xyz"

# Step 3: Motor control parameters
# Sample values taken for calculation (distance in meters, time in seconds)
distance = 5.0
time = 2.0

# Step 4: Motor speed calculation
# Given logic: speed = distance / time
speed = distance / time

# Step 5: Output result (as per instructions)
print("Output:", speed, "m/s")
print("Industry: Apple Robotics")

#OUTPUT 
Output: 2.5 m/s
Industry: Apple Robotics
