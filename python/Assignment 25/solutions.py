# # solution 1

# n = int(input("Enter a number "))
# l1 = []
# if(n>0):
#     for i in range(1,n+1):
#         l1.append(i)
# print(l1)

# # solution 2
# l2=[]
# fterm = 0
# secondterm = 1

# for i in range(n):
#     nexterm = fterm + secondterm
#     l2.append(nexterm)
#     fterm = secondterm
#     secondterm = nexterm

# print(l2)

# # solution 3
# l3 =[]
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         l3.append(i)

# print(l3)

# solution 4

# matrix1 =[[1,2,3],[4,5,6],[7,8,9]]
# matrix2 =[[1,2,3],[4,5,6],[7,8,9]]

# result =[[0,0,0],[0,0,0],[0,0,0]]

# for i in range(0,3):
#     for j in range(0,3):
#         result[i][j] = matrix1[i][j] + matrix2[i][j]
#         print(result[i][j],end=" ")
#     print()

# print()

# solution 5
list1=[1,2,3,-2,-1]

positive = []
negative = []

for i in list1:
    if i<0:
        negative.append(i)
    else:
        positive.append(i)
print(negative)
print(positive)