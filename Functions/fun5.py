# function to test prime or not


def prime(n):
    x = 1
    for i in range(2, n):
        if n % i == 0:
            x = 0
            break
        else:
            x = 1
    return x


# test if a number is prime or not
num = int(input('Enter a number : '))

result = prime(num)
if result == 1:
    print(num, 'is a prime')
else:
    print(num, 'is not prime')

