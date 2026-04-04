# SESSION 39 – NVIDIA (IMU Drift Correction)

# Step 1: Import library
import pandas as pd

# Step 2: Simulated dataset (IMU Drift Dataset)
# Represents orientation drift over time

data = {
    "measured_orientation": [45.0],   # degrees (raw IMU reading)
    "drift": [1.8]                   # degrees (error)
}

dataset = pd.DataFrame(data)

print("Using Dataset: IMU Drift Dataset (Kalibr Simulation)")
print(dataset)

# Step 3: Extract values
measured_orientation = dataset["measured_orientation"][0]
drift = dataset["drift"][0]

# Step 4: Apply drift correction
corrected_orientation = measured_orientation - drift

# Step 5: Display results
print("\nMeasured Orientation:", measured_orientation, "°")
print("Drift:", drift, "°")
print("Corrected Orientation:", corrected_orientation, "°")

print("Output: Orientation Stabilized")

#OUTPUT

Measured Orientation: 45.0 °
Drift: 1.8 °
Corrected Orientation: 43.2 °
Output: Orientation Stabilized
