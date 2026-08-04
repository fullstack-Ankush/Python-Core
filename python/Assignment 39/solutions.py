# solution 1 sum of N natural number 
def sumN(n):
    if n == 0:
        return 0
    return n + sumN(n - 1)

print(sumN(10))

# solution 2 num of N odd natural number 
def sumoddN(n):
    if n < 0:
        return 0
    if n%2 == 1:
        return n + sumoddN(n-2)

print(sumoddN(5))

# solution 3 num of N even natural number 
def sumEvenN(n):
    if n<0:
        return 0
    if n%2 == 0:
        return n + sumEvenN(n-2)

print(sumEvenN(10))

# solution 4 print sqaure of N natural number 

def sumSqaureN(n):
    if n < 0:
        return 1
    return n**2 + sumSqaureN(n-1)

print(sumSqaureN(5))

# solution 5 print cubes of N natural number 

def sumCubesN(n):
    if n<0:
        return 1
    return n**3 + sumCubesN(n-1)