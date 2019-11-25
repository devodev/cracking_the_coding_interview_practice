
def compute_perms(s):
    if s is None:
        return None
    permutations = []
    if not s:
        permutations.append('')
        return permutations
    first = s[0]
    remainder = s[1:]
    words = compute_perms(remainder)
    for word in words:
        for i in range(len(word)+1):
            perm = word[0:i] + first + word[i:]
            permutations.append(perm)
    return permutations


if __name__ == '__main__':
    '''
    Permutations without Dups: Write a method to compute all permutations of a string of unique
    characters.
    '''
    a = 'ab'
    b = 'abc'
    c = 'abcd'
    d = 'abcde'
    print(str(compute_perms(a)))
    print(str(compute_perms(b)))
    print(str(compute_perms(c)))
    print(str(compute_perms(d)))
