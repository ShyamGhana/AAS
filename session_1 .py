# SESSION 1 – NVIDIA (Robot Classification)
# Dataset: UCI HAR (Human Activity Recognition)

# Step 1: Import required libraries
import os
import numpy as np
import pandas as pd
import zipfile
import urllib.request

# Step 2: Download the UCI HAR dataset
dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.zip"
dataset_zip = "UCI_HAR_Dataset.zip"

urllib.request.urlretrieve(dataset_url, dataset_zip)

# Step 3: Extract the dataset
with zipfile.ZipFile(dataset_zip, 'r') as zip_ref:
    zip_ref.extractall()

# Step 4: Load motion feature data (accelerometer & gyroscope signals)
# Using training accelerometer data as motion features

acc_x = pd.read_csv(
    "UCI HAR Dataset/train/Inertial Signals/total_acc_x_train.txt",
    delim_whitespace=True,
    header=None
)

acc_y = pd.read_csv(
    "UCI HAR Dataset/train/Inertial Signals/total_acc_y_train.txt",
    delim_whitespace=True,
    header=None
)

acc_z = pd.read_csv(
    "UCI HAR Dataset/train/Inertial Signals/total_acc_z_train.txt",
    delim_whitespace=True,
    header=None
)

# Step 5: Extract velocity (simple proxy using acceleration magnitude)
acc_magnitude = np.sqrt(acc_x**2 + acc_y**2 + acc_z**2)
velocity = acc_magnitude.mean().mean()

# Step 6: Extract altitude proxy
# Assumption: vertical acceleration (Z-axis) represents altitude change
altitude = acc_z.mean().mean()

# Step 7: Rule-based classifier (as given in instructions)
if altitude > 0:
    robot_type = "Aerial Autonomous Robot"
else:
    robot_type = "Ground Robot"

# Step 8: Output results
print("Robot Type:", robot_type)
print("Industry: NVIDIA Jetson Drone Systems")


#OUTPUT 

Robot Type: Aerial Autonomous Robot
Industry: NVIDIA Jetson Drone Systems
