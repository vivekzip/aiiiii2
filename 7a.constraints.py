class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def is_safe(self, v, color, c):
        return all(self.graph[v][i] == 0 or color[i] != c for i in range(self.V))

    def solve_util(self, m, color, v):
        if v == self.V:
            return True
        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.solve_util(m, color, v + 1):
                    return True
                color[v] = 0
        return False

    def solve(self, m):
        color = [0] * self.V
        if self.solve_util(m, color, 0):
            print("Solution exists: ", *color)
        else:
            print("No solution")

# Example usage
g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
g.solve(3)
