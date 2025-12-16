from collections import deque

def shortest_path(flight_space, start, goal):
    rows, cols = len(flight_space), len(flight_space[0])
    (start_x, start_y), (goal_x, goal_y) = start, goal

    direction =[(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start_x, start_y,[(start_x, start_y)])])
    visited = [[False] *cols for _ in range(rows)]
    visited[start_x][start_y] = True

    while queue:
        print(queue)
        x, y, path = queue.popleft()

        if (x, y) == (goal_x, goal_y):
            return path

        for direction_x, direction_y in direction:
            next_x, next_y = x + direction_x, y + direction_y
            if 0 <= next_x < rows and 0 <= next_y < cols:
                if not visited[next_x][next_y] and grid[next_x][next_y] == 0:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, path + [(next_x, next_y)]))



if __name__ == "__main__":

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    start = (0,0)
    end = (4,4)
    path = shortest_path(grid, start, end)
    print(path)