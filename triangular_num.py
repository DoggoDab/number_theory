def triangular(num): 
    return ((num ** 2) + num) // 2

num = int(input("Enter a number: "))
print(f"T{num} = {triangular(num)}")