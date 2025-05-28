def max_independent_set(nums):
    if not nums:
        return []

    # Check if elements are negative, return empty list if true
    if all(num < 0 for num in nums):
        return []

    n = len(nums)
    if n == 1:
        return [nums[0]] if nums[0] > 0 else []

    # Initialize DP table
    dp = [0] * n  # dp[i] stores max sum up to index i
    dp[0] = max(0, nums[0])  # 1st element is itself or 0 if negative
    dp[1] = max(dp[0], nums[1]) if nums[1] > 0 else dp[0]  # 2nd element choice

    # Fill DP table
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # Choose to include/exclude current element

    # Backtrack to find the elements in the subsequence
    result = []
    i = n - 1
    while i >= 0:
        if i == 0 or (dp[i] != dp[i - 1]):  # If current element contributes to max sum
            if nums[i] > 0:  # Ensure only positive numbers are included
                result.append(nums[i])
            i -= 2  # Skip previous element to maintain non-consecutiveness
        else:
            i -= 1  # Move to previous element

    # Reverse to maintain original order
    return result[::-1]
