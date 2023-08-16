def square_root(num, power): 
    return (num ** power) ** ((1/2))

def cube_root(num, power): 
    return (num ** power) ** ((1/3))

num = int(input("Enter the number: "))
power = int(input("Enter an exponent/indice: "))
print("\n".join([f"Square Root: {square_root(num, power)}", f"Cube Root: {cube_root(num, power)}"]))