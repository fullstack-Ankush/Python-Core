#solution 1
num = [1,2,3,4]
sum = 0
for i in num:
    sum += i
print(sum)

#solution 2
avg = sum/len(num)

#solution 3
sqnum = []
for i in num:
    sqnum.append(i*i)
print(sqnum)

#Solution 4
num.sort(reverse="True")
print(num)

#Solution 5
n = [1,2,3,4,5,6,7,8,9,10]
evenN= []
for i in range(len(n)):
    if(i%2 ==0):    
        evenN.append(n[i])

print(evenN)
