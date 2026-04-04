# SESSION 38 – WALMART (Logistics / Delivery System)

# Step 1: Import library
import pandas as pd

# Step 2: Simulated dataset (Logistics Robot Dataset)
# Represents delivery task execution times

data = {
    "delivery_time_sec": [95]  # seconds
}

dataset = pd.DataFrame(data)

print("Using Dataset: Logistics Robot Dataset (Warehouse Simulation)")
print(dataset)

# Step 3: Extract value
time_taken = dataset["delivery_time_sec"][0]

# Step 4: Define delivery window
max_allowed_time = 100  # seconds

# Step 5: Delivery completion check
if time_taken <= max_allowed_time:
    result = "Package Delivered"
else:
    result = "Delivery Failed"

# Step 6: Display results
print("\nDelivery Time:", time_taken, "seconds")
print("Allowed Time:", max_allowed_time, "seconds")
print("Result:", result)

#OUTPUT

Delivery Time: 95 seconds
Allowed Time: 100 seconds
Result: Package Delivered
