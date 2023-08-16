def odd_or_even():
    nums = []
    while True: 
        num = int(input("Enter your numbers: "))
        if num == 6675239876: 
            break

        nums.append(num)

    return ["Even" if num % 2 == 0 else "Odd" for num in nums]

print(odd_or_even())