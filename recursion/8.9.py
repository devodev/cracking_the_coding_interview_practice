

def get_combinations(n):
    l = []
    _get_combinations(l, n, n, [None]*(n*2), 0)
    return l


def _get_combinations(l, left, right, s, n):
    if left < 0 or right < left:
        return None
    if left == 0 and right == 0:
        l.append(''.join(s))
    else:
        if left > 0:
            s[n] = '('
            _get_combinations(l, left-1, right, s, n+1)
        if right > left:
            s[n] = ')'
            _get_combinations(l, left, right-1, s, n+1)


if __name__ == '__main__':
    '''
    Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
    of n pairs of parentheses.
    '''
    print(get_combinations(-1))
    print(get_combinations(1))
    print(get_combinations(2))
    print(get_combinations(3))
    print(get_combinations(4))
