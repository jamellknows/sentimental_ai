import numpy as np

# Create a random array
array = np.random.randint(1, 100, (5, 5))
print(array)

# Calculate the shortest distance for each row
shortest_distances = np.amin(array, axis=1)

# Calculate the longest distance for each row
longest_distances = np.amax(array, axis=1)

# Print the shortest distances
print("Shortest distances:")
print(shortest_distances)

# Print the longest distances
print("Longest distances:")
print(longest_distances)
