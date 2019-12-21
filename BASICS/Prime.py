num = int(input("ENTER THE VALUE : "))

if num>1:
    for i in range(2, num):
        if (num%i) == 0:
            print("Number is not a primenumber")
        else:
            print("number is prime")
else:
    print("Number is not a primenumber")
