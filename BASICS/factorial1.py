n = int(input("Enter the value : "))


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


result = fact(n)
print("factorial of", n,"is", result)