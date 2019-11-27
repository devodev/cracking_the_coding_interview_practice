

def find_magic_index(a):
    for idx in range(len(a)):
        if idx == a[idx]:
            return idx
    return None


def find_magic_index_optimized(a):
    idx = 0
    while idx < len(a):
        v = a[idx]
        if idx == v:
            return idx
        idx = v if v > idx else idx + 1
    return None


def find_magic_index_rec(a):
    if not a:
        return None
    return _find_magic_index_rec(a, 0, len(a)-1)


def _find_magic_index_rec(a, start, end):
    if end < start:
        return None
    mid = int((start + end) / 2)
    v = a[mid]
    if v == mid:
        return mid
    if v > mid:
        return _find_magic_index_rec(a, start, mid-1)
    return _find_magic_index_rec(a, mid+1, end)


if __name__ == '__main__':
    '''
    Magic Index: A magic index in an array A[0... n-1] is defined to be an index such that A[i] = i.
    Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
    array A.
    '''
    a = [-12, -5, -3, 2, 4, 9]
    b = [0, 1, 4, 5, 6, 7]
    c = [2, 3, 4, 5, 6, 7]
    d = [-1, 0, 1, 2, 3, 5]
    print(find_magic_index_rec(a))
    print(find_magic_index_rec(b))
    print(find_magic_index_rec(c))
    print(find_magic_index_rec(d))