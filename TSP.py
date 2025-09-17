from itertools import permutations
from math import inf

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[-1]][route[0]]
    return total_distance

def brute_force_tsp(distances):
    n = len(distances)
    cities = list(range(1, n))
    shortest_route = None
    min_distance = float('inf')
    
    for perm in permutations(cities):
        current_route = [0] + list(perm)
        current_distance = calculate_distance(current_route, distances)
        
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = current_route
    
    shortest_route.append(0)
    return shortest_route, min_distance

distances = [
    [0, 5900, 6200, 7900, 5200, 4900, 6300, 8000],
    [6700, 0, 6200, 4200, 4500, 7000, 5300, 5900],
    [7500, 5700, 0, 9400, 4000, 4100, 10500, 650],
    [7500, 4300, 10200, 0, 8500, 11600, 1900, 9800],
    [5200, 4700, 2200, 8400, 0, 4000, 9500, 4100],
    [6700, 6500, 3600, 10200, 4000, 0, 11200, 4400],
    [4900, 5600, 10100, 1900, 11800, 8900, 0, 11100],
    [7900, 6100, 250, 9800, 4500, 3800, 10900, 0]
]

route, total_distance = brute_force_tsp(distances)
route = [alphabet[i] for i in route]
print("Route:", route)
print("Total distance:", total_distance)