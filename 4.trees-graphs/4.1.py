
def is_path_exist(g, n, target, memo=None):
    if not g:
        return None
    if n < 0 or n > len(g)-1 or target < 0 or target > len(g[n])-1:
        return None
    if memo is None:
        memo = dict()
    if (n, target) in memo:
        return False
    memo[(n, target)] = g[n][target]
    if memo[(n, target)]:
        return True
    else:
        for i in range(len(g[n])):
            if g[n][i]:
                if is_path_exist(g, i, target, memo):
                    return True
        return False


if __name__ == '__main__':
    '''
    Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
    route between two nodes.

    graph1 = [
        [False, True]
    ]
    graph = 0->1

    graph2 = [
        [False, True, False],
        [False, False, True],
        [True, False, False],
    ]
    graph = 0->1
            ^  |
            |  v
              2
    '''


    graph1 = [
        [False, True]
    ]
    graph2 = [
        [False, True, False],
        [False, False, True],
        [True, False, False],
    ]
    graph3 = [
        [False, True, False, False, True, True],
        [False, False, False, True, True, False],
        [False, True, False, False, False, False],
        [False, False, True, False, True, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
    ]
    print(is_path_exist(graph1, 0, 1))
    print(is_path_exist(graph2, 0, 2))
    print(is_path_exist(graph3, 0, 2))
    print(is_path_exist(graph3, 4, 0))
    print(is_path_exist(graph3, 3, 5))
    print(is_path_exist(None, 3, 5))
    print(is_path_exist(graph3, -1, 5))
