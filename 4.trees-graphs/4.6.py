
class Node(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


def successor(node):
    if not node:
        return None
    if node.right:
        return left_most_child(node.right)
    else:
        q = node
        x = node.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x


def left_most_child(node):
    if not node:
        return None
    n = node
    while n.left:
        n = n.left
    return n


if __name__ == '__main__':
    '''
    Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
    binary search tree. You may assume that each node has a link to its parent.
    '''

    node1 = Node(4)
    node1.left = Node(2)
    node1.left.parent = node1
    node1.left.left = Node(1)
    node1.left.left.parent = node1.left
    node1.left.right = Node(3)
    node1.left.right.parent = node1.left
    node1.right = Node(6)
    node1.right.parent = node1
    node1.right.left = Node(5)
    node1.right.left.parent = node1.right
    node1.right.right = Node(7)
    node1.right.right.parent = node1.right

    tests = [
        (successor(node1), node1.right.left.value),
        (successor(node1.left), node1.left.right.value),
        (successor(node1.left.right), node1.value)
    ]
    try:
        for test, expectation in tests:
            assert getattr(test, 'value', None) == expectation
    except AssertionError:
        print('Test failed')
    else:
        print('Success')
