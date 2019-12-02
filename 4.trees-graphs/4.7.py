

def reorder(items, deps):
    result = []
    graph = build_graph(items, deps)
    while len(result) < len(items):
        nodeps = node_wo_deps(graph, result)
        if not nodeps:
            return None
        for i in nodeps:
            result.append(i)
            for k in graph:
                if i in graph[k]:
                    graph[k].remove(i)
    return result


def build_graph(items, deps):
    graph = {}
    for i in items:
        graph[i] = []
    for d in deps:
        graph[d[1]].append(d[0])
    return graph


def node_wo_deps(graph, result):
    return [k for k, v in graph.items() if k not in result and not v]


if __name__ == '__main__':
    '''
    Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
    projects, where the second project is dependent on the first project). All of a project's dependencies
    must be built before the project is. Find a build order that will allow the projects to be built. If there
    is no valid build order, return an error.
    EXAMPLE
    Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
    Output: f, e, a, b, d, c
    '''

    tests = [
        (
            (
                ['a', 'b', 'c', 'd', 'e', 'f'],
                [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
            ),
            ['e', 'f', 'a', 'b', 'd', 'c']
        )
    ]
    try:
        for test, expectation in tests:
            result = reorder(*test)
            assert result == expectation
    except AssertionError:
        print('Test failed')
    else:
        print('Success')
