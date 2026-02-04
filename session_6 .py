# SESSION 6 – GOOGLE (ROS2 Communication)
# Dataset: ROS2 TurtleBot Logs

# Step 1: Import required libraries
import os
import subprocess
import time

# Step 2: Clone TurtleBot3 repository (ROS2 logs & structure)
repo_url = "https://github.com/ROBOTIS-GIT/turtlebot3.git"
repo_name = "turtlebot3"

if not os.path.exists(repo_name):
    subprocess.run(["git", "clone", repo_url])

# Step 3: Simulate Twist message (Publish)
twist_message = {
    "linear_x": 0.2,
    "angular_z": 0.0
}

print("Publishing Twist Message...")
time.sleep(1)

# Step 4: Simulate Subscriber receiving Twist and executing motion
received_twist = twist_message

if received_twist["linear_x"] > 0:
    robot_status = "Robot Moves"
else:
    robot_status = "Robot Stopped"

# Step 5: Output result (as per instructions)
print("Output:", robot_status)
print("Industry: Google Robotics")
