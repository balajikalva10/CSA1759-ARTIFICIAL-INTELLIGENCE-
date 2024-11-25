from collections import deque

def print_puzzle(state):
    for i in range(0, 9, 3): print(" ".join(state[i:i+3]))
    print("-" * 18)  # Line separator

def get_neighbors(state):
    zero = state.index("0")
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dr, dc in moves:
        r, c = divmod(zero, 3)
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            swap = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[swap] = new_state[swap], new_state[zero]
            neighbors.append("".join(new_state))
    return neighbors

def solve_puzzle(start):
    queue, visited = deque([(start, [])]), set()
    while queue:
        state, path = queue.popleft()
        if state == "123456780": return path
        if state in visited: continue
        visited.add(state)
        for next_state in get_neighbors(state):
            queue.append((next_state, path + [next_state]))
    return None

start = input("Enter initial state (e.g., 123456780): ")
if len(start) != 9 or set(start) != set("012345678"):
    print("Invalid input.")
else:
    solution = solve_puzzle(start)
    if solution:
        print("Solution in", len(solution), "steps:")
        for step in solution: print_puzzle(step)
    else:
        print("No solution.")
