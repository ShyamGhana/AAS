# SESSION 11 – AMAZON (Object Area using COCO Dataset)

# Step 1: Install required libraries
!pip install opencv-python matplotlib

# Step 2: Import libraries
import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np

# Step 3: Download a sample COCO dataset image
image_url = "http://images.cocodataset.org/val2017/000000000139.jpg"
image_path = "coco_sample.jpg"

urllib.request.urlretrieve(image_url, image_path)

# Step 4: Read image
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 5: Define bounding box (Width = 60, Height = 30)
width = 60
height = 30

# Top-left corner of bounding box
x, y = 50, 50

# Step 6: Draw bounding box on image
cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)

# Step 7: Calculate area
area = width * height

# Step 8: Show results
print("Width :", width, "px")
print("Height:", height, "px")
print("Bounding Box Area:", area, "px²")

# Step 9: Display image
plt.imshow(img)
plt.title("COCO Dataset Image with Bounding Box")
plt.axis('off')
plt.show()

#OUTPUT

Width : 60 px
Height: 30 px
Bounding Box Area: 1800 px²
