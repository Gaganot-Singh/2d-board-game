
from a1_partc import Queue

def get_overflow_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    overflow_cells = []

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] >= 0:
                cell_value = grid[row][col]
            else:
                cell_value = -grid[row][col]
            neighbors = 0

            if row > 0:
                neighbors += 1
            if row < rows - 1:
                neighbors += 1
            if col > 0:
                neighbors += 1
            if col < cols - 1:
                neighbors += 1

            if cell_value >= neighbors:
                overflow_cells.append((row, col))

    if not overflow_cells:
        return None
    else:
        return overflow_cells


def overflow(grid, a_queue):
    def spread_overflow(row, col, is_negative):
        neighbors = [
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
        ]

        for r, c in neighbors:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if is_negative:
                    if grid[r][c] >= 0:
                        grid[r][c] = -(grid[r][c]) - 1
                    else:
                        grid[r][c] = -(-grid[r][c]) - 1 
                else:
                    if grid[r][c] >= 0:
                        grid[r][c] = (grid[r][c]) + 1
                    else:
                        grid[r][c] = (-grid[r][c]) + 1 

    overflow_list = get_overflow_list(grid)
    
    if not grid:
        return 0
    
    all_non_negative = True
    for row in grid:
        for x in row:
            if x < 0:
                all_non_negative = False
                break
        if not all_non_negative:
            break
    if all_non_negative:
        return 0


    all_non_positive = True
    for row in grid:
        for x in row:
            if x > 0:
                all_non_positive = False
                break
        if not all_non_positive:
            break
    if all_non_positive:
        return 0
    
    if not overflow_list:
        return 0

    is_negative = grid[overflow_list[0][0]][overflow_list[0][1]] < 0
    for r, c in overflow_list:
        grid[r][c] = 0

    for r, c in overflow_list:
        spread_overflow(r, c, is_negative)

    a_queue.enqueue([row[:] for row in grid])
    return 1 + overflow(grid, a_queue)