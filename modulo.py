def modulo(dividend, divisor, quotient): 
    return dividend % (quotient * divisor)

de = int(input("Enter the dividend: "))
q = int(input("Enter the quotient: "))
di = int(input("Enter the divisor: "))
print(f"{modulo(de, di, q)} is (modulo {di})")