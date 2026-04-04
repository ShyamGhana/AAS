# SESSION 12 – GOOGLE (Place Recognition) – FIXED VERSION

# Step 1: Install libraries
!pip install matplotlib opencv-python

# Step 2: Import libraries
import cv2
import matplotlib.pyplot as plt
import urllib.request

# Step 3: Use a reliable image (GitHub raw image – no 403)
image_url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"
image_path = "sample_place.jpg"

urllib.request.urlretrieve(image_url, image_path)

# Step 4: Read and display image
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.title("Sample Place Image")
plt.axis('off')
plt.show()

# Step 5: Given values
similarity = 0.94
threshold = 0.9

# Step 6: Place recognition logic
if similarity > threshold:
    recognized = True
    result = "Place Recognized"
else:
    recognized = False
    result = "Place Not Recognized"

# Step 7: Output
print("Similarity Score:", similarity)
print("Threshold:", threshold)
print("Result:", result)

#OUTPUT

Similarity Score: 0.94
Threshold: 0.9
Result: Place Recognized
