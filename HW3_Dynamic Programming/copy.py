def dna_match_topdown(DNA1, DNA2):
    """Find length of LCS between 2 DNA sequences using recursive top-down approach with memoization"""
    memo = dict()  # Storing results of subproblems
    return lcs_helper(DNA1, DNA2, len(DNA1), len(DNA2), memo)


def lcs_helper(DNA1, DNA2, i, j, memo):
    """Helper function to compute LCS recursively with memoization"""
    # Return cached result if available
    if (i, j) in memo:
        return memo[(i, j)]
    # Base case - one sequence is empty
    if i == 0 or j == 0:
        memo[(i, j)] = 0
    # If character match, increment LCS count
    elif DNA1[i - 1] == DNA2[j - 1]:
        memo[(i, j)] = 1 + lcs_helper(DNA1, DNA2, i - 1, j - 1, memo)
    # Otherwise, take max of excluding one character from either sequence
    else:
        memo[(i, j)] = max(lcs_helper(DNA1, DNA2, i, j - 1, memo), lcs_helper(DNA1, DNA2, i - 1, j, memo))
    return memo[(i, j)]


def dna_match_bottomup(DNA1, DNA2):
    """Find length of LCS between 2 DNA sequences using iterative bottom-up approach"""
    m, n = len(DNA1), len(DNA2)
    # Initialize table to store LCS lengths
    dp_table = [[0] * (n + 1) for _ in range(m + 1)]  # create a table with all 0s

    # Fill table iteratively
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If character match, increment LCS count
            if DNA1[i - 1] == DNA2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            # Take max value from adjacent cells
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

    # LCS length is in cell
    return dp_table[m][n]


DNA1 = "ATAGTTCCGTCAAA"
DNA2 = "GTGTTCCCGTCAAA"

print("Top-down result:", dna_match_topdown(DNA1, DNA2))
print("Bottom-up result:", dna_match_bottomup(DNA1, DNA2))
