# SESSION 37 – AMAZON (Patrolling / Waypoint Navigation)

# Step 1: Import libraries
import pandas as pd
import time

# Step 2: Simulated dataset (Waypoint Navigation Dataset)
# Represents predefined patrol points

data = {
    "waypoint_x": [0, 2, 4, 2, 0],
    "waypoint_y": [0, 2, 0, -2, 0]
}

dataset = pd.DataFrame(data)

print("Using Dataset: Waypoint Navigation Dataset (ROS2 Nav2 Simulation)")
print(dataset)

# Step 3: Patrol logic (cyclic navigation)
print("\nStarting Patrol...\n")

for cycle in range(2):  # simulate 2 cycles (can be infinite in real system)
    print(f"--- Patrol Cycle {cycle+1} ---")
    
    for i in range(len(dataset)):
        wp = (dataset["waypoint_x"][i], dataset["waypoint_y"][i])
        print(f"Navigating to Waypoint {i+1}: {wp}")
        time.sleep(0.5)  # simulate movement delay

print("\nOutput: Continuous Patrol")

#OUTPUT

Using Dataset: Waypoint Navigation Dataset (ROS2 Nav2 Simulation)
   waypoint_x  waypoint_y
0           0           0
1           2           2
2           4           0
3           2          -2
4           0           0

Starting Patrol...

--- Patrol Cycle 1 ---
Navigating to Waypoint 1: (np.int64(0), np.int64(0))
/usr/local/lib/python3.12/dist-packages/jupyter_client/session.py:203: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  return datetime.utcnow().replace(tzinfo=utc)
Navigating to Waypoint 2: (np.int64(2), np.int64(2))
Navigating to Waypoint 3: (np.int64(4), np.int64(0))
Navigating to Waypoint 4: (np.int64(2), np.int64(-2))
Navigating to Waypoint 5: (np.int64(0), np.int64(0))
--- Patrol Cycle 2 ---
Navigating to Waypoint 1: (np.int64(0), np.int64(0))
Navigating to Waypoint 2: (np.int64(2), np.int64(2))
Navigating to Waypoint 3: (np.int64(4), np.int64(0))
Navigating to Waypoint 4: (np.int64(2), np.int64(-2))
Navigating to Waypoint 5: (np.int64(0), np.int64(0))

Output: Continuous Patrol
