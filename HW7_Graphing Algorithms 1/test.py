def minEffort(puzzle):
    # Get the number of rows and columns in the puzzle
    m = len(puzzle)
    n = len(puzzle[0])

    # Create a queue with the starting point (0, 0) and the effort required to reach that point (which is 0)
    queue = [(0, 0, 0)]

    # Create a dictionary to keep track of the minimum effort required to reach each point on the puzzle
    # Initialize the starting point's minimum effort to 0
    min_effort = {(0, 0): 0}

    # Create a list of neighboring points (up, down, left, right) to traverse in BFS
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Perform BFS traversal
    while queue:
        # Dequeue a point from the queue
        x, y, effort = queue.pop(0)

        # Check if we have reached the destination point (m-1, n-1)
        if x == m - 1 and y == n - 1:
            # If yes, return the minimum effort required to reach that point
            return min_effort[(x, y)]

        # Check neighboring points and add them to the queue if they have not been visited yet
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            # Check if the neighboring point is within the bounds of the puzzle
            if 0 <= nx < m and 0 <= ny < n:
                # Calculate the new effort required to reach the neighboring point
                new_effort = max(effort, abs(puzzle[nx][ny] - puzzle[x][y]))
                # Check if the neighboring point has not been visited yet, or if the new effort required to reach it is less than the previously calculated minimum effort
                if (nx, ny) not in min_effort or new_effort < min_effort[(nx, ny)]:
                    # Update the minimum effort required to reach the neighboring point in the dictionary
                    min_effort[(nx, ny)] = new_effort
                    # Add the neighboring point to the queue with the new effort required to reach it
                    queue.append((nx, ny, new_effort))

    # If we reach here, it means we were unable to reach the destination point
    return -1


# Example usage:
puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(minEffort(puzzle))  # Output: 1