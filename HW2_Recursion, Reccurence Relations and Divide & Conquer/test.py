def kthElement(Arr1, Arr2, k):
    # Ensure Arr1 is the smaller array
    if len(Arr1) > len(Arr2):
        return kthElement(Arr2, Arr1, k)

    # Base cases
    if len(Arr1) == 0:
        return Arr2[k - 1]  # Return kth element from Arr2

    if k == 1:
        return min(Arr1[0], Arr2[0])  # Return the smallest of the first elements

    # Partition the arrays
    index1 = min(len(Arr1), k // 2)
    index2 = k - index1
    value1 = Arr1[index1 - 1]
    value2 = Arr2[index2 - 1]

    # Eliminate part of one array
    if value1 <= value2:
        return kthElement(Arr1[index1:], Arr2, k - index1)
    else:
        return kthElement(Arr1, Arr2[index2:], k - index2)

# Example usage
if __name__ == "__main__":
    Arr1 = [1, 2, 3, 5, 6]
    Arr2 = [3, 4, 5, 6, 7]
    k = 5
    print(f"The {k}-th element is: {kthElement(Arr1, Arr2, k)}")