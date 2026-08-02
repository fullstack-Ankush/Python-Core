# solution 1 print N odd numbers
def printOddNumbers(n):
    for i in range(1, n*2, 2):
        print(i, end= " ")

# solution 2 print N prime numbers

def printPrimeNumbers(n):
    count = 0
    num =  2
    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end= " ")
            count += 1
        num += 1        

# solution 3 print prime number between 2 numbers
def printPrimeNumbersBetween(a, b):
    for num in range(a, b + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end= " ")

printPrimeNumbersBetween(10, 50)    
# solution 4 

def FirstNfibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end= " ")
        a, b = b, a + b

# solution 5 print all the fctors of   number
def printFactors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end= " ")


    