# SESSION 21 – NVIDIA (Reinforcement Learning - Q-Learning)

# Step 1: Install OpenAI Gym (Dataset/Environment)
!pip install gym

# Step 2: Import libraries
import gym

# Step 3: Load dataset (environment)
env = gym.make("FrozenLake-v1", is_slippery=False)

# Reset environment
state = env.reset()

print("Using Dataset: OpenAI Gym - FrozenLake Environment")

# Step 4: Given values
reward = 8
learning_rate = 0.5

# Step 5: Initialize Q-value
Q_old = 0

# Step 6: Q-learning update
Q_new = Q_old + learning_rate * (reward - Q_old)

# Step 7: Output
print("Reward:", reward)
print("Learning Rate:", learning_rate)
print("Updated Q-value:", Q_new)

#OUTPUT

Using Dataset: OpenAI Gym - FrozenLake Environment
Reward: 8
Learning Rate: 0.5
Updated Q-value: 4.0
