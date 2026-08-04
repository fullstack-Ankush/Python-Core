# solution 1

def sumDigits(n):
    if n//10 == 0:
        return n
    return n%10 + sumDigits(n//10)

print(sumDigits(1234))

# solution 2 

def factorial(n):
    if n  == 0:
        return 1
    return n * factorial(n-1)

# solution 3 ,4,5

# Can't do this 