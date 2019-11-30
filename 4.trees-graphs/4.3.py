

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_lists(tree):
    result = []
    _create_lists(tree, 0, result)
    return result


def _create_lists(node, level, result):
    if not node:
        return None
    if len(result) <= level:
        result.append([])
    result[level].append(node.value)
    _create_lists(node.left, level+1, result)
    _create_lists(node.right, level+1, result)


if __name__ == '__main__':
    '''
    List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
    '''
    node1 = Node(1)
    node1.left = Node(2)
    node1.left.left = Node(10)
    node1.left.right = Node(11)
    node1.right = Node(3)
    node1.right.left = Node(20)
    node1.right.left.left = Node(200)
    node1.right.left.right = Node(2000)
    node1.right.left.right.left = Node(20000)
    node1.right.right = Node(21)

    print(create_lists(node1))
