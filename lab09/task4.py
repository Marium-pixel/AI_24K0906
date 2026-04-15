import numpy as np

#task 4

np.random.seed(42)

states = ["Sunny", "Cloudy", "Rainy"]

transition_matrix = np.array([
    [0.60, 0.30, 0.10],
    [0.30, 0.40, 0.30],
    [0.20, 0.30, 0.50],
])

def simulate_weather(initial_state, num_days):
    current = initial_state
    sequence = [current]
    idx = {s: i for i, s in enumerate(states)}

    for _ in range(num_days - 1):
        probs = transition_matrix[idx[current]]
        current = np.random.choice(states, p=probs)
        sequence.append(current)

    return sequence

# Simulation
sequence = simulate_weather("Sunny", 10)
print("\nWeather Sequence:")
print(" -> ".join(sequence))

# Monte Carlo
count = 0
simulations = 100000

for _ in range(simulations):
    sim = simulate_weather("Sunny", 10)
    if sim.count("Rainy") >= 3:
        count += 1

prob = count / simulations
print(f"\nP(at least 3 rainy days) = {prob:.4f}")
