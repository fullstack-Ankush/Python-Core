# solution 1
l1 = [1,2,2,3,4,5,6,6,5,5,3,]
result = set(l1)
print(result)

# solution 2
set1 = {1,2,3,4,5,6,7,8,9,10}
evenset = set()
oddset = set()
for e in set1:
    if e%2 == 0:
        evenset.add(e)
    else:
        oddset.add(e)
print(evenset,oddset)

# solution 3
result = set()
playerset = {"Ankush","Amit","Kartik","Dhruv","Omkar"}
# write a script to print all possibilities of a player playing with other players in the set.
for player in playerset:
    for opponent in playerset:
        if player != opponent:
            result.add((player,opponent))
print(result)
            
# solution 5
result = set()
ti = tuple()
num = int(input("Enter a number less than 12: "))
for i in range(1,7):
    for j in range(1,7):
        if i+j == num:
            ti = (i,j)
            result.add(ti)
print(result)