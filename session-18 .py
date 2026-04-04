# SESSION 18 – IBM (Rule-Based Agent)

# Step 1: Define environment conditions
obstacle_detected = True
speed = 5   # current speed (> 0)

# Step 2: Apply rule
if obstacle_detected and speed > 0:
    action = "Stop"
else:
    action = "Move"

# Step 3: Display result
print("Obstacle Detected:", obstacle_detected)
print("Current Speed:", speed)
print("Action:", action)

# Step 4: Final Output
if action == "Stop":
    print("Stop Action Executed")

#OUTPUT

Obstacle Detected: True
Current Speed: 5
Action: Stop
Stop Action Executed
