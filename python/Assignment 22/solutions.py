# solution 1 
result = 0
n = int(input("Enter a number"))
for i in range(1,n+1):
    result += i
print(result)

# solution 2
sqaureSum = 1
for i in range(1,n+1):
    sqaureSum += i**2

print(sqaureSum)

# solution 3
cudeSum = 1
for i in range(1,n+1):
    cudeSum += i**3

#solution 4
oddSum = 0
for i in range(1,n+1,2):
    oddSum += i
print(oddSum)


#solution 5
evenSum = 0
for i in range(2,n+1,2):
    evenSum += i
print(evenSum)
