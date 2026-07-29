# solution 1 
sample1 = "Myhomie"

print(sample1.isalpha())

# solution 2
targetchar = (input("Enter a char"))
sample2 = "ankush"
if targetchar in sample2:
    print(True)
else:
    print(False)

# solution 3
count = 0
sample3 = "Education".lower()
for i in sample3:
    if i in ['a','e','i','o','u']:
        count += 1

print(count)


# solution 4
count = 0
sample4="romio1234"
for i in sample4:
    if(i.isalpha()):
        count += 1
    else:
        None

print(count)

# solution 5
sample5 = "ankush"
print(sample5[::-1])