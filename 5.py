from collections import deque

def is_valid(state):
    m_left, c_left, m_right, c_right = state
    return 0 <= m_left <= 3 and 0 <= c_left <= 3 and m_left >= c_left and m_right >= c_right

def solve_missionaries_cannibals():
    start, goal = (3, 3, 0, 0), (0, 0, 3, 3)
    visited, queue = set(), deque([(start, [])])

    while queue:
        state, path = queue.popleft()
        if state in visited: continue
        visited.add(state)
        
        if state == goal:
            for step in path + [state]: print(step)
            return

        m_left, c_left, m_right, c_right = state
        moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
        for m, c in moves:
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c) if m + c <= 2 else None
            if new_state and is_valid(new_state): queue.append((new_state, path + [state]))
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c) if m + c <= 2 else None
            if new_state and is_valid(new_state): queue.append((new_state, path + [state]))

    print("No solution.")

solve_missionaries_cannibals()
