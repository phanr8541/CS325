def kthElement(Arr1, Arr2, k):
    # Base Case 1: If the first array is empty, the k-th element must be in the second array
    if len(Arr1) == 0:
        return Arr2[k - 1]

    # Base Case 2: If the second array is empty, the k-th element must be in the first array
    if len(Arr2) == 0:
        return Arr1[k - 1]

    # Calculate the middle indices of the two arrays
    midx1 = len(Arr1) // 2
    midx2 = len(Arr2) // 2

    # Compare the middle elements of both arrays to decide which part to discard
    if Arr1[midx1] <= Arr2[midx2]:
        # If the combined size of the left halves (mid1 + mid2 + 1) is greater than or equal to k,
        # the k-th element lies in the left part of one or both arrays.
        if k <= midx1 + midx2 + 1:
            # Recur on the entire first array and the left half of the second array
            return kthElement(Arr1, Arr2[:midx2], k)
        else:
            # Otherwise, discard the left half of the first array and adjust k
            return kthElement(Arr1[midx1 + 1:], Arr2, k - midx1 - 1)
    else:
        # If the combined size of the left halves (mid1 + mid2 + 1) is greater than or equal to k,
        # the k-th element lies in the left part of one or both arrays.
        if k <= midx1 + midx2 + 1:
            # Recur on the left half of the first array and the entire second array
            return kthElement(Arr1[:midx1], Arr2, k)
        else:
            # Otherwise, discard the left half of the second array and adjust k
            return kthElement(Arr1, Arr2[midx2 + 1:], k - midx2 - 1)

