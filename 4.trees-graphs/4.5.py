
class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_bst(node):
    return _check_bst(node, None, None)


def _check_bst(n, mi, ma):
    if n is None:
        return True
    if (mi and n.value <= mi) or (ma and n.value > ma):
        return False
    if not _check_bst(n.left, mi, n.value) or not _check_bst(n.right, n.value, ma):
        return False
    return True

if __name__ == '__main__':
    '''
    Validate BST: Implement a function to check if a binary tree is a binary search tree.
    '''

    node1 = Node(4)
    node1.left = Node(2)
    node1.left.left = Node(1)
    node1.left.right = Node(3)
    node1.right = Node(6)
    node1.right.left = Node(5)
    node1.right.right = Node(7)

    node2 = Node(4)
    node2.left = Node(5)
    node2.left.left = Node(1)
    node2.left.right = Node(3)
    node2.right = Node(8)
    node2.right.left = Node(7)
    node2.right.right = Node(9)

    tests = [
        (check_bst(node1), True),
        (check_bst(node2), False)
    ]
    try:
        for test, expectation in tests:
            assert test == expectation
    except AssertionError:
        print('Test failed')
    else:
        print('Success')
