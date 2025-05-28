def feedDog(hunger_level, biscuit_size):
    """Determine max number of dogs that can be satisfied given hunger level and available biscuit sizes"""
    # Sort hunger levels and biscuit sizes
    hunger_level.sort()
    biscuit_size.sort()

    dog_index = 0  # Pointer for hunger_level
    biscuit_index = 0  # Pointer for biscuit_size
    satisfied_dogs = 0  # Counter for satisfied dogs

    # Iterate through biscuits while there are dogs left
    while dog_index < len(hunger_level) and biscuit_index < len(biscuit_size):
        if biscuit_size[biscuit_index] >= hunger_level[dog_index]:
            # Current biscuit can satisfy current dog
            satisfied_dogs += 1
            dog_index += 1  # Move to the next dog
        biscuit_index += 1  # Move to the next biscuit

    return satisfied_dogs


# Example 1
hunger_level1 = [1, 2, 3]
biscuit_size1 = [1, 1]
print(feedDog(hunger_level1, biscuit_size1))  # Output: 1

# Example 2
hunger_level2 = [2, 1]
biscuit_size2 = [1, 3, 2]
print(feedDog(hunger_level2, biscuit_size2))  # Output: 2