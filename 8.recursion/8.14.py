

def count_ways(expr, result):
    if not expr:
        return 0
    if len(expr) == 1:
        return 1 if get_bool(expr) == result else 0
    ways = 0
    for i in range(1, len(expr), 2):
        sign = expr[i]
        left = expr[0:i]
        right = expr[i+1:]

        left_true = count_ways(left, True)
        left_false = count_ways(left, False)
        right_true = count_ways(right, True)
        right_false = count_ways(right, False)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if sign == '^':
            total_true = (left_true * right_false) + (left_false * right_true)
        elif sign == '&':
            total_true = left_true * right_true
        elif sign == '|':
            total_true = (left_true * right_true) + (left_false * right_true) + (left_true * right_false)

        subways = total_true if result else total - total_true
        ways += subways
    return ways


def get_bool(char):
    return char == '1'


if __name__ == '__main__':
    '''
    Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true),
    & (AND), | (OR), and ^ (XOR), and a desired boolean result value result, implement a function to
    count the number of ways of parenthesizing the expression such that it evaluates to result.
    EXAMPLE
    countEval('1^0|0|1', false) -> 2
    countEval('0&0&0&1^1|0', true) -> 10
    '''
    tests = [
        ('1^0|0|1', False),
        ('0&0&0&1^1|0', True)
    ]
    for idx, t in enumerate(tests, 1):
        print('{}. {}\nResult: {}'.format(idx, t, count_ways(*t)))
