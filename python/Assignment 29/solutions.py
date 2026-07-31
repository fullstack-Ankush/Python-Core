# solution 1
t1 = tuple([1,2,3,4])
print(t1)

# solution 2
t1 = 2,3,4,5

print(t1[::-1])

# solution 3
stringList = ["Ankush","Amit","Rishu","Ashish"]

    

resultList = []



# solution 4 
sample4 = "Ankush"
resultList = []

for i in sample4:
    tuple1 = (i,ord(i))
    resultList.append(tuple1)
print(resultList)

# solution 5
oddTuple = (1,2,13,4,5,6,7,8,9)
result = 0

for i in oddTuple:
    if i%2 == 1:
        result += i

print(result)