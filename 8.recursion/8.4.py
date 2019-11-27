

def get_subsets(s):
    if not s:
        return None
    return _get_subsets(s, 0)


def _get_subsets(s, n):
    all_subsets = None
    if len(s) == n:
        all_subsets = []
        all_subsets.append(set())
    else:
        all_subsets = _get_subsets(s, n+1)
        item = s[n]
        more_subsets = []
        for subset in all_subsets:
            new_subset = subset.copy()
            new_subset.add(item)
            more_subsets.append(new_subset)
        all_subsets.extend(more_subsets)
    return all_subsets
    

if __name__ == '__main__':
    '''
    Power Set: Write a method to return all subsets of a set.
    '''
    subsets = {
        'a': [0, 1, 2, 3, 4],
        'b': [0, 1, 2, 3],
        'c': [0, 1, 2],
        'd': [0, 1],
        'e': [0],
    }
    asc_sort = lambda x: len(x)
    for key, subset in subsets.items():
        print('{}. P({}) = {}'.format(key, str(subset), str(sorted(get_subsets(subset), key=asc_sort))))