# SESSION 8 – META (Camera Projection)
# Dataset: ETH3D Camera Dataset

# Step 1: Import required libraries
import numpy as np

# Step 2: Include dataset source in code
dataset_url = "https://www.eth3d.net/datasets"

# Step 3: Define projection formula
# Condition: u = f * X / Z

f = 300      # focal length
X = 1        # object coordinate
Z = 1        # depth

# Step 4: Compute camera projection
u = f * X / Z

# Step 5: Output result (as per instructions)
print("Output:", int(u), "px")
print("Industry: AR/VR Systems")
