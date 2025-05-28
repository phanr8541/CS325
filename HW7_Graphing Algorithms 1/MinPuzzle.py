def minEffort(puzzle):
    # Check if the puzzle is empty
    if not puzzle or not puzzle[0]:
        return 0

    m, n = len(puzzle), len(puzzle[0])  # Dimensions of the puzzle
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible movement directions (Up, Down, Left, Right)

    # Initialize the effort matrix where effort[i][j] represents the minimal effort to reach cell (i, j)
    effort_matrix = [[float('inf')] * n for _ in range(m)]
    effort_matrix[0][0] = 0  # The starting cell has 0 effort (no movement)

    # Priority queue (min-heap) to store cells in the form (effort, row, col)
    # Initially, only the starting cell is in the queue
    priority_queue = [(0, 0, 0)]  # (effort, row, col)

    while priority_queue:
        # Pop the cell with the smallest effort from the priority queue
        current_effort, row, col = pop_min(priority_queue)

        # If we have reached the bottom-right corner, return the minimal effort required
        if row == m - 1 and col == n - 1:
            return current_effort

        # Explore the four possible neighbors (Up, Down, Left, Right)
        for d_row, d_col in directions:
            neighbor_row, neighbor_col = row + d_row, col + d_col

            # Check if the neighbor is within bounds
            if 0 <= neighbor_row < m and 0 <= neighbor_col < n:
                # Calculate the effort to move to the neighbor cell
                new_effort = max(current_effort, abs(puzzle[neighbor_row][neighbor_col] - puzzle[row][col]))

                # If a better path to the neighbor is found, update the effort and add it to the queue
                if new_effort < effort_matrix[neighbor_row][neighbor_col]:
                    effort_matrix[neighbor_row][neighbor_col] = new_effort
                    priority_queue.append((new_effort, neighbor_row, neighbor_col))  # Add neighbor to the queue

    return -1  # Return -1 if no path exists (should never happen in a connected grid)


def pop_min(priority_queue):
    """Custom function to simulate popping the element with the smallest effort from the priority queue (min-heap).
    It scans the queue, finds the smallest element, and removes it."""
    min_effort = float('inf')
    min_index = -1
    for i in range(len(priority_queue)):
        if priority_queue[i][0] < min_effort:
            min_effort = priority_queue[i][0]
            min_index = i
    return priority_queue.pop(min_index)  # Remove and return the element with the smallest effort

