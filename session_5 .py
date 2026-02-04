# SESSION 5 – MICROSOFT (AI Model Choice)
# Dataset: UCI Iris Dataset

# Step 1: Import required libraries
import pandas as pd
import numpy as np
import urllib.request

# Step 2: Dataset URL (UCI Iris Dataset)
iris_dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
print("Dataset Source:", iris_dataset_url)

# Step 3: Load the dataset
column_names = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "class_label"
]

iris_data = pd.read_csv(iris_dataset_url, header=None, names=column_names)

# Step 4: Detect labeled data
# Checking if class label column exists
if "class_label" in iris_data.columns:
    labeled_data = True
else:
    labeled_data = False

# Step 5: Select ML type based on data
if labeled_data:
    model_type = "Classification Model"
else:
    model_type = "Clustering Model"

# Step 6: Output result (as per instructions)
print("Output:", model_type)
print("Industry: Azure ML")
