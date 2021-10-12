import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b ** 2 - 4 * a * c
x1 = x2 = int()

if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
elif D == 0:
    x1 = -b / 2 * a
    x2 = -b / 2 * a
else:
    pass

print(int(x1), int(x2), sep='\n')