def divisibility(num, numBy): 
    return num % numBy == 0

def divideByDivisibility(num, numBy): 
    return num / numBy

num = int(input("Enter a number: "))
numBy = int(input("Enter a number divisible by: "))
if divisibility(num, numBy): 
    print(f"{num} is divisible by {numBy}")
    print(f"Result: {divideByDivisibility(num, numBy)}")

else: 
    print(f"{num} isn't divisible by {numBy}")
    print(f"Result: {divideByDivisibility(num, numBy)}")