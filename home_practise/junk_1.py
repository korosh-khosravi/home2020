width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]


a = [min(width[i[0]:i[1] + 1]) for i in cases]


print(a)

    # a = [width[j] for j in range(i[0], i[1])]