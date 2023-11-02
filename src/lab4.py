def read_input(file_path):
    matrix = []
    with open(file_path, 'r') as f:
        for line in f:
            row = [int(x) for x in line.strip()]
            matrix.append(row)
    return matrix


def is_valid(x, y, visited, matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return 0 <= x < rows and 0 <= y < columns and matrix[x][y] and not (x, y) in visited


def shortest_path(matrix):
    if not matrix:
        return -1

    rows = len(matrix)
    columns = len(matrix[0])
    visited = []
    queue = []

    for i in range(rows):
        if matrix[i][0] == 1:
            queue.append((i, 0, 0, [(i, 0)]))
            visited.append((i, 0))

    while queue:
        x, y, dist, current_path = queue.pop(0)
        if y == columns - 1:
            return dist

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, visited, matrix):
                new_path = current_path + [(new_x, new_y)]
                queue.append((new_x, new_y, dist + 1, new_path))
                visited.append((new_x, new_y))
    return -1


def write_result(result, output_path):
    with open(output_path, 'w') as f:
        f.write(str(result))
