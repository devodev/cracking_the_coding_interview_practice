
def print_ways(size, r, columns, results):
    if r == size:
        results.append(columns[:])
        return
    for i in range(size):
        if valid(columns, r, i):
            columns[r] = i
            print_ways(size, r+1, columns, results)


def valid(columns, r, c):
    for r2 in range(r):
        c2 = columns[r2]
        if c2 == c:
            return False
        col_distance = abs(c-c2)
        row_distance = r-r2
        if col_distance == row_distance:
            return False
    return True


if __name__ == '__main__':
    '''
    Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
    so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
    diagonals, not just the two that bisect the board.

    Q,Q,Q,Q,Q,Q,Q,Q
    [
        [X,X,X,X,X,X,X,X],
        [X,X,X,X,X,X,X,X],
        [X,X,X,X,X,X,X,X],
        [X,X,X,X,X,X,X,X],
        [X,X,X,X,X,X,X,X],
        [X,X,X,X,X,X,X,X],
        [X,X,X,X,X,X,X,X],
        [X,X,X,X,X,X,X,X]
    ]
    [
        [Q,X,X,X,X,X,X,X],
        [X,X,Q,X,X,X,X,X],
        [X,X,X,X,Q,X,X,X],
        [X,X,X,X,X,X,Q,X],
        [X,Q,X,X,X,X,X,X],
        [X,X,X,Q,X,X,X,X],
        [X,X,X,X,X,Q,X,X],
        [X,X,X,X,X,X,X,Q]
    ]
    '''
    size = 8
    columns = [None]*size
    results = []
    print_ways(size, 0, columns, results)
    print(results)
