from collections import deque


def solve_puzzle(board, source, destination):
    # Directions: Left, Right, Up, Down
    directions = [(-1, 0, 'L'), (1, 0, 'R'), (0, -1, 'U'), (0, 1, 'D')]

    # Base case: if the source is the same as destination
    if source == destination:
        return [source], ''

    # Check if source or destination is blocked
    if board[source[0]][source[1]] == '#' or board[destination[0]][destination[1]] == '#':
        return None

    # Initialize BFS
    queue = deque([(source, [], '')])  # stores (current_position, path_so_far, direction_so_far)
    visited = set()
    visited.add(source)

    while queue:
        (x, y), path, direction = queue.popleft()

        # Check each direction (in the order: L, R, U, D)
        for dx, dy, dir_char in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == '-' and (nx, ny) not in visited:
                # If destination found, return the path and directions
                if (nx, ny) == destination:
                    return path + [(x, y), (nx, ny)], direction + dir_char
                # Otherwise, add the new position to the queue
                queue.append(((nx, ny), path + [(x, y)], direction + dir_char))
                visited.add((nx, ny))



    # If no path is found
    return None