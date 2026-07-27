# solution 1

n = int(input("Enter a number"))
factorial  = 1

while(n):
    if(n == 0):
        print("Factorial is 1 ")
        break
    else:
        for i in range(1,n+1):
            factorial *= i
        break

print(factorial)

# solution 2
n = str(1234)
count = 0

for i in n:
    if (i in n):
        count += 1
print(count)

# print(type(n))

#solution 3
sum = 0
n = 1234
for i in range(count):

    sum += n%10
    n = n//10

print(sum)

#solution 4
n = 4

#solution 5

