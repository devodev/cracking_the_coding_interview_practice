
class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_balanced(node):
    if not node:
        return None
    return _is_balanced(node) != -1


def _is_balanced(node):
    if not node:
        return 0
    left_height = _is_balanced(node.left)
    if left_height == -1:
        return -1
    right_height = _is_balanced(node.right)
    if right_height == -1:
        return -1
    delta = left_height - right_height
    if delta < -1 or delta > 1:
        return -1
    return (left_height if left_height > right_height else right_height) +1


if __name__ == '__main__':
    '''
    Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
    node never differ by more than one.
    '''
    node1 = Node(1)
    node1.left = Node(2)
    node1.left.left = Node(8)
    node1.right = Node(3)
    node1.right.right = Node(4)
    node1.right.right.right = Node(5)
    node1.right.right.right.left = Node(10)

    node2 = Node(1)
    node2.left = Node(2)
    node2.left.left = Node(8)
    node2.right = Node(3)

    node3 = Node(1)

    node4 = None

    node5 = Node(1)

    node5.left = Node(2)
    node5.left.left = Node(8)
    node5.left.left.left = Node(8)
    node5.left.left.right = Node(8)
    node5.left.right = Node(8)
    node5.left.right.left = Node(8)
    node5.left.left.right.left = Node(8)
    node5.right = Node(3)
    node5.right.left = Node(4)
    node5.right.left.left = Node(4)
    node5.right.right = Node(4)
    node5.right.right.left = Node(5)
    node5.right.right.right = Node(5)
    node5.right.right.right.left = Node(10)

    try:
        assert is_balanced(node1) == False
        assert is_balanced(node2) == True
        assert is_balanced(node3) == True
        assert is_balanced(node4) == None
        assert is_balanced(node5) == True
    except AssertionError:
        print('Test failed')
    else:
        print('Success')
