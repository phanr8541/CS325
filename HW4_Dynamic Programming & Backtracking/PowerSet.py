def powerset(inputSet):
    """Generate powerset (all subsets) of a given set"""
    result = []  # Stores all subsets
    backtrack(0, inputSet, [], result)  # Start the recursive backtracking process
    return result


def backtrack(start, inputSet, currentSet, result):
    """Recursively generates subsets using backtracking"""
    result.append(currentSet[:])  # Append a copy of current subset to the result

    # Iterate over remaining elements
    for i in range(start, len(inputSet)):
        currentSet.append(inputSet[i])  # Include current element in subset
        backtrack(i + 1, inputSet, currentSet, result)  # Recurse with next index
        currentSet.pop()  # Remove last elements before next iteration (backtrack)

