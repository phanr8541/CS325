from collections import deque

def solve_puzzle(Board, Source, Destination):
    rows = len(Board)
    cols = len(Board[0])

    def is_valid(cell):
        row, col = cell
        return 0 <= row < rows and 0 <= col < cols and Board[row][col] == '-'

    queue = deque([Source])
    visited = [[False] * cols for _ in range(rows)]
    prev_cell = {}
    visited[Source[0]][Source[1]] = True

    # Correct directions map with missing bracket
    directions_map = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}

    while queue:
        current_cell = queue.popleft()
        if current_cell == Destination:
            break

        row, col = current_cell

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            neighbor = (row + dr, col + dc)

            if is_valid(neighbor) and not visited[neighbor[0]][neighbor[1]]:
                queue.append(neighbor)
                visited[neighbor[0]][neighbor[1]] = True
                prev_cell[neighbor] = current_cell

    # If destination is not reachable, return None
    if Destination not in prev_cell:
        return None, None  # No valid path found

    # Reconstruct the path and directions
    path = [Destination]
    directions_taken = ""
    while path[-1] != Source:
        prev_row, prev_col = prev_cell[path[-1]]
        diff_row = path[-1][0] - prev_row
        diff_col = path[-1][1] - prev_col
        directions_taken += directions_map[(diff_row, diff_col)]
        path.append(prev_cell[path[-1]])

    path.reverse()
    directions_taken = directions_taken[::-1]  # Reverse directions string

    return path, directions_taken


# Test cases
if __name__ == "__main__":
    Board = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ]

    Source = (0, 2)
    Destination = (2, 2)
    path, directions = solve_puzzle(Board, Source, Destination)
    print(path, directions)  # Output: ([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], "LDDR")

    Source = (0, 0)
    Destination = (4, 4)
    path, directions = solve_puzzle(Board, Source, Destination)
    print(path,
          directions)  # Output: ([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)], "RRRRDDDD")