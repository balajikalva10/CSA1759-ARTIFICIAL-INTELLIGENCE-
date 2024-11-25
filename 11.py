map_graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
colors = ['Red', 'Green', 'Blue']

def is_valid(region, color, assignment):
    return all(assignment.get(neighbor) != color for neighbor in map_graph[region])

def map_coloring(assignment={}):
    if len(assignment) == len(map_graph): return assignment
    region = next(r for r in map_graph if r not in assignment)
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            if map_coloring(assignment): return assignment
            del assignment[region]
    return None

def solve():
    result = map_coloring()
    if result: 
        print("\n".join(f"{r}: {c}" for r, c in result.items()))
    else: 
        print("No solution found")

solve()
