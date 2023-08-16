def verify_prime(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i += 6
    return True

def prime(nums):
    primes = []
    for num in nums:
        if verify_prime(num): 
            primes.append(num)
    return primes

def composite(nums): 
    composites = []
    for num in nums: 
        if not verify_prime(num): 
            composites.append(num)
    return composites

nums = []
while True: 
    num = int(input("Enter your numbers: "))
    if num == 667234598671: 
        break

    nums.append(num)

p = prime(nums)
c = composite(nums)

print("\n".join([f"Prime Numbers: {p}", f"Composite Numbers: {c}"]))