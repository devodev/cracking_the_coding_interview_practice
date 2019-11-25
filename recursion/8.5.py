

def multiply_rec(a, b):
    '''
    O(min(a,b))
    '''
    small = a if a < b else b
    big = b if a < b else a
    if small == 0:
        return 0
    return big + multiply_rec(big, small-1)


def multiply_rec2(a, b):
    '''
    O(?)
    '''
    small = a if a < b else b
    big = b if a < b else a
    return _multiply_rec2(small, big, dict())


def _multiply_rec2(small, big, memo):
    if small == 0:
        return 0
    if small == 1:
        return big
    if small in memo:
        return memo[small]
    half = small >> 1
    side1 = _multiply_rec2(half, big, memo)
    side2 = side1
    if small % 2 == 1:
        side2 = _multiply_rec2(small - half, big, memo)
    memo[small] = side1 + side2
    return memo[small]


def multiply_rec3(a, b):
    '''
    O(log(min(a,b)))
    '''
    small = a if a < b else b
    big = b if a < b else a
    return _multiply_rec3(small, big)


def _multiply_rec3(small, big):
    if small == 0:
        return 0
    if small == 1:
        return big
    half = small >> 1
    side1 = _multiply_rec3(half, big)
    if small % 2 == 0:
        return side1 + side1
    else:
        return side1 + side1 + big


if __name__ == '__main__':
    '''
    Recursive Multiply: Write a recursive function to multiply two positive integers without using the
    * operator. You can use addition, subtraction, and bit shifting, but you should minimize the number
    of those operations.
    '''
    values = [(0, 1), (1, 0), (1, 1), (2, 4), (4, 2), (13, 4), (11, 11)]
    for a, b in values:
        print('{} * {} = {}'.format(a, b, multiply_rec(a, b)))
    for a, b in values:
        print('{} * {} = {}'.format(a, b, multiply_rec2(a, b)))
    for a, b in values:
        print('{} * {} = {}'.format(a, b, multiply_rec3(a, b)))