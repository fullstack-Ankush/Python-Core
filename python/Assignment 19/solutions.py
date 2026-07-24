# #solution 1 
# user = input("Enter your string ")
# # for i in user:
# #     print("unicode of %c is %i"%(i,ord(i)))

# # solution 2
# vowels = 0
# for i in user :
#     if(i =='a' or i == 'e' or i =='i' or i == 'o' or i =='u'):
#         vowels += 1
# print(vowels)

# #solution 3
# spaceCount = 0
# for i in user:
#     if i == " ":
#         spaceCount += 1
# print(spaceCount)

#solution 4
index = 0
n = input("Enter your number")
s=''
for i in n:
    if(i not in s):
        s += i
        print(i,end="")



# solution 5

# digits = input("Enter digits ")
# for i in digits :
#     n += 1
# print(n)