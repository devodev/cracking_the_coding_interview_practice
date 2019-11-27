

class Color(object):

    def __init__(self, c):
        self.c = c
        self.visited = False

    def __eq__(self, other):
        return self.c == other.c

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return str(self.c)


def fill(screen, point, new_color, original=None):
    if any(x is None for x in (screen, point, new_color)):
        return None
    if (point[0] < 0 or point[0] > len(screen)-1
        or point[1] < 0 or point[1] > len(screen[0])-1
    ):
        return None
    color = screen[point[0]][point[1]]
    if color.visited:
        return None
    color.visited = True
    if original is None:
        original = Color(color.c)
    if color != original:
        return None

    color.c = new_color.c
    fill(screen, (point[0]-1, point[1]),   new_color, original)
    fill(screen, (point[0]+1, point[1]),   new_color, original)
    fill(screen, (point[0],   point[1]-1), new_color, original)
    fill(screen, (point[0],   point[1]+1), new_color, original)


if __name__ == '__main__':
    '''
    Paint Fill: Implement the "paint Fill" function that one might see on many image editing programs.
    That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
    fill in the surrounding area until the color changes from the original color.
    '''
    screen = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    screen = [[Color(screen[i][y]) for y in range(len(screen[i]))] for i in range(len(screen))]
    print('\n'.join(str(x) for x in screen))
    print('---')
    point = (3, 3)
    new_color = Color(255)
    fill(screen, point, new_color)
    print('\n'.join(str(x) for x in screen))
