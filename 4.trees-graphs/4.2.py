

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        '''pre-order traversal'''
        return '--'.join((
            'v:{}'.format(str(self.value)),
            'l:{}'.format(str(self.left)),
            'r:{}'.format(str(self.right))))


def build_bst(arr):
    return _build_bst(arr, 0, len(arr)-1)

def _build_bst(arr, start, end):
    if end < start:
        return None
    index = int((start+end+1)/2) # +1 to balance to the left
    mid = arr[index]
    node = Node(mid)
    node.left = _build_bst(arr, start, index-1)
    node.right = _build_bst(arr, index+1, end)
    return node


if __name__ == '__main__':
    '''
    Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
    to create a binary search tree with minimal height.
    '''

    tests = [
        [],
        [0],
        [0, 1],
        [0, 1, 2, 3, 4],
        [0, 4, 8, 9, 11],
        [2, 4, 6, 8, 10, 20]
    ]
    for t in tests:
        print(build_bst(t))
