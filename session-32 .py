# SESSION 32 – MICROSOFT (ROS2 Python)

# Step 1: Import libraries
import time
import pandas as pd

# Step 2: Simulated dataset (ROS2 rclpy Publisher Logs)
# Represents timestamps of published messages

message_rate = 15  # Hz
interval = 1.0 / message_rate

timestamps = []

print("Using Dataset: ROS2 rclpy Publisher Logs (Simulation)")

# Step 3: Simulate publishing messages
start_time = time.time()

for i in range(10):  # simulate 10 messages
    current_time = time.time()
    timestamps.append(current_time)
    print(f"Publishing message {i} at time {round(current_time, 4)}")
    time.sleep(interval)

end_time = time.time()

# Step 4: Convert to dataset
dataset = pd.DataFrame({"timestamps": timestamps})

# Step 5: Calculate actual frequency
total_time = end_time - start_time
actual_rate = len(timestamps) / total_time

print("\nCalculated Frequency:", round(actual_rate, 2), "Hz")

# Step 6: Check real-time performance
if actual_rate >= 14:   # allow small tolerance
    result = "Real-Time Performance Achieved"
else:
    result = "Performance Not Achieved"

#OUTPUT
Using Dataset: ROS2 rclpy Publisher Logs (Simulation)
Publishing message 0 at time 1775319918.5745
Publishing message 1 at time 1775319918.6413
Publishing message 2 at time 1775319918.7082
Publishing message 3 at time 1775319918.7751
Publishing message 4 at time 1775319918.842
Publishing message 5 at time 1775319918.9089
Publishing message 6 at time 1775319918.9757
Publishing message 7 at time 1775319919.0429
Publishing message 8 at time 1775319919.1098
Publishing message 9 at time 1775319919.1767

Calculated Frequency: 14.93 Hz
Result: Real-Time Performance Achieved


print("Result:", result)
