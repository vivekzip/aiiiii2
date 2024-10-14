import random
import numpy as np

def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

def generate_matrix(coordinate):
    return [[distance(p1, p2) for p2 in coordinate] for p1 in coordinate]

def random_solution(matrix):
    return random.sample(range(len(matrix)), len(matrix))

def path_length(matrix, solution):
    return sum(matrix[solution[i-1]][solution[i]] for i in range(len(solution)))

def hill_climbing(coordinate):
    matrix = generate_matrix(coordinate)
    current_solution = random_solution(matrix)
    current_path = path_length(matrix, current_solution)
    
    while True:
        neighbor = random.sample(range(len(matrix)), len(matrix))
        neighbor_path = path_length(matrix, neighbor)
        if neighbor_path < current_path:
            current_solution = neighbor
            current_path = neighbor_path
        else:
            break
    
    return current_path, current_solution

coordinate = np.array([[1,2], [30,21], [56,23], [8,18], [20,50], [3,4], [11,6], [6,7], [15,20], [10,9], [12,12]])
final_solution = hill_climbing(coordinate)
print("The solution is \n", final_solution[1])
