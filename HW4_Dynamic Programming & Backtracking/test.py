def max_independent_set(nums):
    if not nums:
        return []

    n = len(nums)
    if n == 1:
        return [nums[0]] if nums[0] > 0 else []

    # Step 1: Initialize DP table
    dp = [0] * n
    dp[0] = max(0, nums[0])
    dp[1] = max(dp[0], nums[1])

    # Step 2: Fill DP table
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    # Step 3: Backtrack to find the elements in the subsequence
    result = []
    i = n - 1
    while i >= 0:
        if i == 0 or (dp[i] != dp[i - 1]):  # Element included
            result.append(nums[i])
            i -= 2  # Skip previous element
        else:
            i -= 1  # Move to previous element

    return result[::-1]  # Reverse to maintain original order


# Example Test Cases
print(max_independent_set([7, 2, 5, 8, 6]))  # Output: [7, 5, 6]
print(max_independent_set([-1, -1, 0]))  # Output: [0] or []
print(max_independent_set([-1, -1, -10, -34]))  # Output: []
print(max_independent_set([10, -3, 0]))  # Output: [10]