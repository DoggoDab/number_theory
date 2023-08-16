def fibonacci(num):
    if num < 0: 
        raise ValueError("Integers should be positive!")

    if num == 0:
        return 0 
    
    elif num == 1:
        return 1
    
    else: 
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input("Enter a number: "))
print(fibonacci(num))