
def move_items(n):
    if n <= 0:
        return None
    a = [x for x in reversed(range(n))]
    b = []
    c = []
    _move_items(n, a, b, c)
    print (n, a, b, c)


def _move_items(n, orig, dest, buf):
    if n == 0:
        return None

    _move_items(n-1, orig, buf, dest)
    item = orig.pop()
    dest.append(item)
    _move_items(n-1, buf, dest, orig)


if __name__ == '__main__':
    '''
    Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
    different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
    of size from top to bottom (Le., each disk sits on top of an even larger one). You have the following
    constraints:
    (1) Only one disk can be moved at a time.
    (2) A disk is slid off the top of one tower onto another tower.
    (3) A disk cannot be placed on top of a smaller disk.
    Write a program to move the disks from the first tower to the last using stacks.
    '''
    print(move_items(3))
    print(move_items(4))
    print(move_items(5))
    print(move_items(10))
    print(move_items(15))
    print(move_items(20))