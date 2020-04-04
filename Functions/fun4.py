# function to calc factorial


def fact(n):
    x = 1
    while n >= 1:
        x *= n
        n -= 1
    return x


for i in range(1, 8):
    print(fact(i))
