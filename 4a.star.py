import heapq

def a_star_search(grid, src, dest):
    open_list = [(0, src)]
    closed_list = set()
    parent_dict = {src: None}
    g_values = {src: 0}
    f_values = {src: calculate_h_value(*src, dest)}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == dest:
            print("The Path is ")
            path = []
            while current:
                path.append(current)
                current = parent_dict[current]
            path.reverse()
            for i in path:
                print("->", i, end=" ")
            print()
            return
        closed_list.add(current)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current[0] + dx, current[1] + dy
            if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])) and grid[new_x][new_y] == 1 and (new_x, new_y) not in closed_list:
                new_g = g_values[current] + 1
                new_f = new_g + calculate_h_value(new_x, new_y, dest)
                if (new_x, new_y) not in f_values or new_f < f_values[(new_x, new_y)]:
                    f_values[(new_x, new_y)] = new_f
                    g_values[(new_x, new_y)] = new_g
                    parent_dict[(new_x, new_y)] = current
                    heapq.heappush(open_list, (new_f, (new_x, new_y)))

    print("Failed to find the destination cell")

def calculate_h_value(x, y, dest):
    return ((x - dest[0]) ** 2 + (y - dest[1]) ** 2) ** 0.5

grid = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
]

src = [8, 0]
dest = [0, 0]
a_star_search(grid, tuple(src), tuple(dest))
