# SESSION 9 – NVIDIA (Image Processing)
# Dataset: CIFAR-10

# Step 1: Import required libraries
import numpy as np

# Step 2: Include dataset source in code
dataset_url = "https://www.cs.toronto.edu/~kriz/cifar.html"

# Step 3: Define RGB values (sample from dataset)
R = 120
G = 180
B = 200

# Step 4: Apply grayscale conversion condition
# gray = 0.3*R + 0.59*G + 0.11*B
gray = 0.3*R + 0.59*G + 0.11*B

# Step 5: Output result (as per instructions)
print("Output:", int(gray))
print("Industry: Vision AI")

#OUTPUT 
Output: 164
Industry: Vision AI
