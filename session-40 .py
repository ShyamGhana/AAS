# SESSION 40 – TESLA (PID Control - Proportional)

# Step 1: Import library
import pandas as pd

# Step 2: Simulated dataset (PID Line Following Dataset)
# Represents tracking error and controller parameters

data = {
    "error": [12],
    "Kp": [0.12]
}

dataset = pd.DataFrame(data)

print("Using Dataset: PID Line Following Dataset (PythonRobotics Simulation)")
print(dataset)

# Step 3: Extract values
error = dataset["error"][0]
Kp = dataset["Kp"][0]

# Step 4: Compute control output (Proportional Control)
control_output = Kp * error

# Step 5: Display results
print("\nError (e):", error)
print("Proportional Gain (Kp):", Kp)
print("Control Output:", control_output)

#OUTPUT

Error (e): 12
Proportional Gain (Kp): 0.12
Control Output: 1.44
