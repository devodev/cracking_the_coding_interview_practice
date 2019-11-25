import sys


def count_ways(n):
    return count_ways_rec(n, dict())


def count_ways_rec(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = count_ways_rec(n-1, memo) + count_ways_rec(n-2, memo) + count_ways_rec(n-3, memo)
    return memo[n]


if __name__ == '__main__':
    """
    Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
    steps at a time. Implement a method to count how many possible ways the child can run up the
    stairs.
    """
    n = int(sys.argv[1])
    print(count_ways(n))