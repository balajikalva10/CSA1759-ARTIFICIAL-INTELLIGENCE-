from collections import deque

def water_jug(x, y, target):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty

    while queue:
        jug1, jug2 = queue.popleft()

        # Skip if state has been visited
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        print(f"Jug1 = {jug1}, Jug2 = {jug2}")

        # Check if target is reached
        if jug1 == target or jug2 == target:
            print("Target achieved!")
            return

        # Possible states
        next_states = [
            (x, jug2),  # Fill Jug1
            (jug1, y),  # Fill Jug2
            (0, jug2),  # Empty Jug1
            (jug1, 0),  # Empty Jug2
            (min(jug1 + jug2, x), max(0, jug1 + jug2 - x)),  # Pour Jug2 -> Jug1
            (max(0, jug1 + jug2 - y), min(jug1 + jug2, y))   # Pour Jug1 -> Jug2
        ]

        # Add new states to the queue
        for state in next_states:
            if state not in visited:
                queue.append(state)

    print("No solution.")

# Input
x, y, target = map(int, input("Enter Jug1 capacity, Jug2 capacity, and target amount: ").split())

# If target exceeds both jugs' capacity, it's impossible
if target > max(x, y):
    print("Target cannot be achieved.")
else:
    water_jug(x, y, target)
