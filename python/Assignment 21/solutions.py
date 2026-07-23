# # solution 1

# n = int(input("Enter a number "))
# for i in range(1,n+1):
#     if(i%2 == 0):
#         print(i)

# # solution 2
# for i in range(1,n+1):
#     if(i%2 == 1):
#         print(i)

# #solution 3
# for i in range(1,n+1):
#     print(i**2)

# # solution 4
# for i in range(1,n+1):
#         print(i**3)
#solution 5

for i in range(15,46):
     for j in range(2,i+1):
          if i%j == 0:
               break
          
          print("%d is prime"%(i))
               
          
