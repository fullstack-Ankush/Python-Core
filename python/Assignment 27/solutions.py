#solution 1
sample1 = "Ankush is back"
s =sample1.split(" ")
r = s[::-1]
for i in r :
    print(i,end=" ")

# solution 2
integer = []
sample2 = "I got 80 marks and 20 marks  in the english and math paper "
s = sample2.split(" ")
for i in s:
    if(i.isnumeric()):
        integer.append(i)

print(integer)

# solution 3
sample3 = "12231"
result = sample3[::-1]

if(sample3 == result):
    print("Yes, Palindrome")
else:
    print("No, It is not Palindrome")

# solution 4

sample4="niggatron"
print(sample4.upper())

# solution 5
#  
sample5 = "Hello NIggatron is there anybody"
s = sample5.split(" ")
lenght = len(s[0])
for i in s:
    if(len(i) > lenght):
        length = len(i)

print(lenght)    


