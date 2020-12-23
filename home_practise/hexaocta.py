n = int(input())
binary_list = []
oct_list = []
hexal_list = []
decimal_list = []


def binary(n):
    c: list = []
    while n // 2 != 0:
        c.append(n % 2)
        n = n // 2
    if n // 2 == 0:
        c.append(n)
    c.reverse()
    return c


def octal(n):

    c: list = []

    while n // 8 != 0:
        c.append(n % 8)
        n = n // 8
    if n // 8 == 0:
        c.append(n)
    c.reverse()
    return c


def hexal(n):

    c: list = []

    while n // 16 != 0:
        c.append(n % 16)
        n = n // 16
    if n // 16 == 0:
        c.append(n)

    for i in range(len(c)):
        if c[i] == 10:
            c.insert(i, 'A')
            c.pop(i + 1)
        elif c[i] == 11:
            c.insert(i, 'B')
            c.pop(i + 1)
        elif c[i] == 12:
            c.insert(i, 'C')
            c.pop(i + 1)
        elif c[i] == 13:
            c.insert(i, 'D')
            c.pop(i + 1)
        elif c[i] == 14:
            c.insert(i, 'E')
            c.pop(i + 1)
        elif c[i] == 15:
            c.insert(i, 'F')
            c.pop(i + 1)

    c.reverse()
    return c


def kcalc(n):
    for i in range(1, n+1):
        b = binary(i)
        binary_list.append(b)
        o = octal(i)
        oct_list.append(o)
        h = hexal(i)
        hexal_list.append(h)
        decimal_list.append(i)
        zipped = zip(decimal_list, oct_list, hexal_list, binary_list)
    return zipped


result = kcalc(n)
print(list(result))
# for i in result:
#     print(*i)