
thickness = 7
height = 21
c = '|'
w = 'WELCOME'
print(c.rjust(5, '@'))
for i in range(thickness//2):
    print((c*i).rjust((height//2), '-') + c.center(3, '.') + (c*i).ljust((height//2), '-'))

print(w.center(height, '-'))


for i in range(thickness//2):
    print((c * ((thickness//2)-i-1)).rjust((height // 2), '-') + c.center(3, '.') + (c * ((thickness//2)-i-1)).ljust((height // 2), '-'))
