def coprime(num1, num2): 
    gcf = 1

    for i in range(1, num1 + 1): 
        if num1 % i == 0 and num2 % i == 0:
            gcf = i 

    return gcf == 1

num1 = int(input("Enter a number: "))
num2 = int(input("Enter an another number: "))
if coprime(num1, num2):
    print(f"{num1} and {num2} are co-prime numbers")

else: 
    print(f"{num1} and {num2} aren't co-prime numbers")