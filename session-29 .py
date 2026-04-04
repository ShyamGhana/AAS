# SESSION 29 – SAUDI ARAMCO (Hybrid Energy System)

# Step 1: Import library
import pandas as pd

# Step 2: Simulated dataset (Battery Health Dataset)
# Represents battery levels of robot system

data = {
    "battery_level": [18]  # percentage
}

dataset = pd.DataFrame(data)

print("Using Dataset: Battery Health Dataset (Kaggle Simulation)")
print(dataset)

# Step 3: Extract battery value
battery = dataset["battery_level"][0]

# Step 4: Define threshold
threshold = 20  # critical battery level (%)

# Step 5: State switching logic
if battery < threshold:
    mode = "Charging Mode"
else:
    mode = "Operational Mode"

# Step 6: Display results
print("\nBattery Level:", battery, "%")
print("Threshold:", threshold, "%")
print("System Mode:", mode)

#OUTPUT

Battery Level: 18 %
Threshold: 20 %
System Mode: Charging Mode
