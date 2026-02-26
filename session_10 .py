# SESSION 10 – TESLA (Edge Detection)
# Dataset: Berkeley Edge Dataset

# Step 1: Import required libraries
import numpy as np

# Step 2: Include dataset source in code
dataset_url = "https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/"

# Step 3: Define gradient values (sample from dataset)
Gx = 5
Gy = 12

# Step 4: Apply edge detection condition
# edge = sqrt(Gx**2 + Gy**2)
edge = np.sqrt(Gx**2 + Gy**2)

# Step 5: Output result (as per instructions)
print("Output:", int(edge))
print("Industry: Autonomous Driving")

#OUTPUT 
Output: 13
Industry: Autonomous Driving
