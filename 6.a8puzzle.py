from heapq import heappush, heappop
import copy

n = 3  # Size of the puzzle (3x3)
moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # Down, Left, Up, Right

class Node:
    def __init__(self, mat, empty_pos, level, cost, parent=None):
        self.mat = mat
        self.empty_pos = empty_pos
        self.level = level
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def calculate_cost(mat, goal):
    return sum(mat[i][j] != goal[i][j] and mat[i][j] != 0 
               for i in range(n) for j in range(n))

def create_node(mat, empty_pos, new_pos, level, parent, goal):
    new_mat = copy.deepcopy(mat)
    x1, y1 = empty_pos
    x2, y2 = new_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    cost = calculate_cost(new_mat, goal) + level
    return Node(new_mat, new_pos, level, cost, parent)

def print_path(node):
    if node:
        print_path(node.parent)
        for row in node.mat:
            print(row)
        print()

def solve(initial, empty_pos, goal):
    pq = []
    root = Node(initial, empty_pos, 0, calculate_cost(initial, goal))
    heappush(pq, root)

    while pq:
        current = heappop(pq)
        if current.cost == current.level:
            print_path(current)
            return
        x, y = current.empty_pos
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                child = create_node(current.mat, (x, y), (nx, ny), 
                                    current.level + 1, current, goal)
                heappush(pq, child)

# Example usage
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
goal = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty_pos = (1, 2)
solve(initial, empty_pos, goal)
