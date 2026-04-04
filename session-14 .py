# SESSION 14 – NVIDIA (Visual SLAM)

# Step 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Define previous pose (x, y)
prev_pose = np.array([2, 3])

# Step 3: Define motion (dx, dy)
motion = np.array([0.4, 0.6])

# Step 4: Compute new pose
new_pose = prev_pose + motion

# Step 5: Display results
print("Previous Pose:", tuple(prev_pose))
print("Motion:", tuple(motion))
print("New Pose:", tuple(new_pose))

# Step 6: Visualization (for understanding)
plt.figure()

# Plot previous position
plt.scatter(prev_pose[0], prev_pose[1], label="Previous Pose")

# Plot new position
plt.scatter(new_pose[0], new_pose[1], label="New Pose")

# Draw arrow showing motion
plt.arrow(prev_pose[0], prev_pose[1], motion[0], motion[1],
          head_width=0.1, length_includes_head=True)

plt.title("Visual SLAM Pose Update")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.grid()

plt.show()

#OUTPUT 

Previous Pose: (np.int64(2), np.int64(3))
Motion: (np.float64(0.4), np.float64(0.6))
New Pose: (np.float64(2.4), np.float64(3.6))
