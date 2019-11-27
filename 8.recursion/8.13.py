

class Box(object):

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    @property
    def tup(self):
        return (self.width, self.height, self.depth)

    def __eq__(self, other):
        return self.tup == other.tup

    def __ne__(self, other):
        return self.tup != other.tup

    def __gt__(self, other):
        return (self.width > other.width
            and self.height > other.height
            and self.depth > other.depth)

    def __repr__(self):
        return '({})'.format(', '.join(str(x) for x in self.tup))


def tallest_stack(s):
    if s is None:
        return None
    s_sorted = sorted(s, reverse=True)
    max_height = 0
    stackmap = [None]*len(s)
    for i in range(len(s)):
        height = _tallest_stack(s_sorted, i, stackmap)
        if height > max_height:
            max_height = height
    return max_height


def _tallest_stack(s, n, stackmap):
    if stackmap[n]:
        return stackmap[n]
    bottom = s[n]
    max_height = 0
    for i in range(n, len(s)):
        top = s[i]
        if bottom > top:
            height = _tallest_stack(s, i, stackmap)
            if height > max_height:
                max_height = height
    max_height += bottom.height
    stackmap[n] = max_height
    return max_height


if __name__ == '__main__':
    '''
    Stack of Boxes: You have a stack of n boxes, with widths wi, heights hi, and depths di. The boxes
    cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
    larger than the box above it in width, height, and depth. Implement a method to compute the
    height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
    '''
    tests = [
        [Box(0,1,0), Box(1,1,1), Box(2,2,2)],
        [Box(0,1,0), Box(1,1,1), Box(2,2,2), Box(1,2,3)],
        [Box(0,1,0), Box(1,1,1), Box(2,2,2), Box(1,2,3), Box(4,4,4), Box(4,4,5)],
        [Box(0,1,0), Box(1,1,1), Box(2,2,2), Box(1,2,3), Box(4,4,4), Box(4,4,5), Box(5,4,5), Box(6,7,6)]
    ]
    for idx, t in enumerate(tests, 1):
        print('{}. {}\nResult: {}'.format(idx, t, tallest_stack(t)))
