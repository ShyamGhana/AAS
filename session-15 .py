# SESSION 15 – MICROSOFT (Kalman Filter)

# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Simulated dataset (prediction + measurement)
prediction = 20
measurement = 24

# Step 3: Kalman Filter Update (Simplified)
estimate = (prediction + measurement) / 2

# Step 4: Display results
print("Prediction:", prediction)
print("Measurement:", measurement)
print("Estimated State:", estimate)

# Step 5: Visualization (for understanding)
labels = ['Prediction', 'Measurement', 'Estimate']
values = [prediction, measurement, estimate]

plt.bar(labels, values)
plt.title("Kalman Filter State Estimation")
plt.ylabel("Value")
plt.show()

#OUTPUT

Prediction: 20
Measurement: 24
Estimated State: 22.0
