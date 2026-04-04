# SESSION 13 – APPLE (Sensor Fusion)

# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Simulate EuRoC MAV dataset readings (IMU + Vision)
# (In real case, these come from sensors)

imu_reading = 32     # degrees
vision_reading = 28  # degrees

# Step 3: Sensor Fusion (Mean Method)
fused_angle = (imu_reading + vision_reading) / 2

# Step 4: Display results
print("IMU Reading:", imu_reading, "°")
print("Vision Reading:", vision_reading, "°")
print("Fused Angle:", fused_angle, "°")

# Step 5: Visualization (optional for understanding)
labels = ['IMU', 'Vision', 'Fused']
values = [imu_reading, vision_reading, fused_angle]

plt.bar(labels, values)
plt.title("Sensor Fusion (IMU + Vision)")
plt.ylabel("Angle (degrees)")
plt.show()

#OUTPUT

IMU Reading: 32 °
Vision Reading: 28 °
Fused Angle: 30.0 °
