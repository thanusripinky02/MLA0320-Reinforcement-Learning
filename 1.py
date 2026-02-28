import numpy as np
import random

# Grid size
GRID_SIZE = 5

# Rewards grid (0 = normal)
grid = np.zeros((GRID_SIZE, GRID_SIZE))

# Define dirt cells (+1)
dirt_cells = [(1,1), (2,3), (4,4)]
for cell in dirt_cells:
    grid[cell] = 1

# Define obstacle cells (-1)
obstacles = [(1,3), (3,2)]
for cell in obstacles:
    grid[cell] = -1

# Actions
actions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

# Check valid move
def is_valid(state):
    r, c = state
    return 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE

# Environment step
def step(state, action):
    dr, dc = actions[action]
    new_state = (state[0] + dr, state[1] + dc)

    if not is_valid(new_state):
        return state, -1   # penalty for hitting wall
    
    reward = grid[new_state]
    return new_state, reward

# Simulate Random Policy
def simulate(steps=20):
    state = (0,0)
    total_reward = 0
    print("Start at:", state)

    for i in range(steps):
        action = random.choice(list(actions.keys()))
        next_state, reward = step(state, action)
        total_reward += reward
        print(f"Step {i+1}: {action} -> {next_state}, Reward: {reward}")
        state = next_state

    print("Total Reward:", total_reward)

simulate()
