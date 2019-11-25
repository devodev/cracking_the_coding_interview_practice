

class Point(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return '({}, {})'.format(self.row, self.col)


def get_path(grid):
    if not grid:
        return None
    path = []
    memo = dict()
    if get_path_rec(grid, len(grid)-1, len(grid[0])-1, path, memo):
        return path
    return None


def get_path_rec(grid, row, col, path, memo):
    if row < 0 or col < 0 or not grid[row][col]:
        return False

    is_origin = row == 0 and col == 0

    p = Point(row, col)

    if p in memo:
        return memo[p]

    success = False
    if (
        is_origin
        or get_path_rec(grid, row, col-1, path, memo)
        or get_path_rec(grid, row-1, col, path, memo)
    ):
        path.append(p)
        success = True
    memo[p] = success
    return success


if __name__ == '__main__':
    """
    Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
    The robot can only move in two directions, right and down, but certain cells are "off limits" such that
    the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
    the bottom right.
    """
    grid = [
        [True, True,  True,  True, False, True],
        [True, True,  False, True, True,  True],
        [True, False, True,  True, False, True],
        [True, True,  True,  True, False, True],
    ]
    print(get_path(grid))