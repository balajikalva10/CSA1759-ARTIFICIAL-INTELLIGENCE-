import heapq

def a_star(start, goal, grid):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_list = [(heuristic(start, goal), 0, start)]  # (f_cost, g_cost, position)
    g_costs = {start: 0}
    came_from = {}

    while open_list:
        _, g_cost, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1] + [current]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_cost = g_cost + 1
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, tentative_g_cost, neighbor))
                    came_from[neighbor] = current

    return None  # No path found

# Simple example
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
start, goal = (0, 0), (2, 2)

# Running the A* algorithm
path = a_star(start, goal, grid)
print("Path:", path if path else "No path found")
