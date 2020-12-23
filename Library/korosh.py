thickness, height = map(int, input().split())


def loop(thickness, height):
    c = '.|.'
    w = 'WELCOME'
    for i in range(thickness//2):
        print((c*i).rjust((height//2)-1, '-') + c + (c*i).ljust((height//2)-1, '-'))

    print(w.center(height, '-'))

    for i in range(thickness//2):
        print((c * ((thickness//2)-i-1)).rjust((height // 2)-1, '-') + c.center(3, '.') + (c * ((thickness//2)-i-1)).ljust((height // 2)-1, '-'))


loop(thickness, height)
