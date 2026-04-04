# SESSION 36 – NVIDIA (Line Detection / Line Following)

# Step 1: Import libraries
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Simulated dataset (OpenCV Line Dataset)
# Represents detected line offset from center

data = {
    "offset_px": [25]   # positive offset (robot drifted right)
}

dataset = pd.DataFrame(data)

print("Using Dataset: OpenCV Line Dataset (Simulation)")
print(dataset)

# Step 3: Extract offset
offset = dataset["offset_px"][0]

# Step 4: Control logic
if offset > 0:
    action = "Turn Left"
elif offset < 0:
    action = "Turn Right"
else:
    action = "Go Straight"

# Step 5: Display results
print("\nOffset:", offset, "px")
print("Action:", action)

# Step 6: Visualization (simulate line position)
img = np.zeros((200, 200, 3), dtype=np.uint8)

# Draw center reference line
cv2.line(img, (100, 0), (100, 200), (0, 255, 0), 2)

# Draw detected line (shifted right → offset +25)
cv2.line(img, (100 + offset, 0), (100 + offset, 200), (255, 0, 0), 2)

plt.imshow(img)
plt.title("Line Detection (Offset Visualization)")
plt.axis('off')
plt.show()

#OUTPUT

Offset: 25 px
Action: Turn Left
