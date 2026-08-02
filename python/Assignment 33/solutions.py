# solution 1
def isevenorOdd(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"

# solution 2
def greaterthan3(a,b,c):
    if a > b and a > c:
        return a 
    elif b>a and b>c:
        return b
    else:
        return c

# solution 3
def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                return "Not prime"
            else:
                return "Prime"

# solution 4

def isleapyear(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return "Leap Year"
            else:
                return "Not a Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not a Leap Year"

# solution 5
def factorial(n): # without any recursion
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact

