import itertools

def tsp(cities, dist_matrix):
    min_distance = float('inf')
    best_route = None
    
    for route in itertools.permutations(cities):
        distance = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        distance += dist_matrix[route[-1]][route[0]]
        
        if distance < min_distance:
            min_distance = distance
            best_route = route
    
    print(f"Optimal Route: {best_route} with distance: {min_distance}")

cities = [0, 1, 2]
dist_matrix = [
    [0, 10, 15],
    [10, 0, 35],
    [15, 35, 0]
]

tsp(cities, dist_matrix)
