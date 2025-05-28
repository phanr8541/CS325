def amount(A, S):
    A.sort()  # Sort to help manage duplicates
    unique_nums = []  # List to store unique numbers from A
    counts = []  # List to store count of each unique number

    # Construct unique elements list and their counts
    for num in A:
        if not unique_nums or unique_nums[-1] != num:
            unique_nums.append(num)  # Add new unique number to list
            counts.append(1)  # Initialize its count to 1
        else:
            counts[-1] += 1  # Increment count if number is already in list

    result = []
    combination_sum_helper(unique_nums, counts, 0, result, S, [])  # Call helper to find combo
    return result


def combination_sum_helper(nums, counts, start, result, remainder, combination):
    """Recursive helper function to find valid combinations that sum up to target"""
    if remainder == 0:
        result.append(combination[:])  # Store a deep copy of the valid combination
        return
    elif remainder < 0:
        return  # Stop if the sum exceeds the target

    for i in range(start, len(nums)):
        if counts[i] > 0:  # Ensure we don’t exceed the allowed occurrences
            combination.append(nums[i])
            counts[i] -= 1  # Decrease available count

            combination_sum_helper(nums, counts, i, result, remainder - nums[i], combination)

            combination.pop()  # Backtrack
            counts[i] += 1  # Restore count


# Example Usage
A = [11, 1, 3, 2, 6, 1, 5]
S = 8
print(amount(A, S))

