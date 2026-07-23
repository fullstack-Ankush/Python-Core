# solutions 1

# x = input("Enter 3 digit number")
# match  x:
#     case x if(len(x) == 3):
#         print("Yes")
#     case _:
#         print("No")


# # solution 2

# match x:
#     case x if(x>0):
#         print("Positive")
#     case x if(x<0):
#         print("Negative")
#     case _:
#         print("zero")

# #solution 3

# print("1.Odd-Even")
# print("2.Positive-NonPositive")
# print("3.Simple interest")
# print("4.roots of quadratic equation")

# y = int(input("Enter a choice from above menu "))

# match y:
#     case 1:
#         a = int(input("Enter a number"))
#         if(a%2==0):
#             print("Even")
#         else:
#             print("Odd")
#     case 2:
#         a = int(input("Enter a number"))
#         if(a>0):
#             print("Positive")
#         else:
#             print("Non-Positive")
#     case 3:
#         p,r,t = int(input("enter principle")),int(input("Enter rate ")),int(input("Enter time in year"))
#         print("Simmple Interst is ",(p*r*t)/100)
#     case 4:
#         a,b,c = int(input("Enter a ")),int(input("Enter b")),int(input("Enter c"))
#         D = (b**2 - 4*a*c)
#         root1,root2 = (-b + D**(1/2))/2*a,(-b-D**(1/2))/2*a
#         print(root1,root2)
#     case _:
#         print("Wrong Key pressed ")


#solution 4
user = eval(input("Enter input"))

match user :
    case user if(type(user) == type(2)):
        print("Monday")
    case user if(type(user) == type(2.1)):
        print("Tuesday")
    case user if(type(user) == type(1+2j)):
        print("Wednesday")
    case user if(type(user) == type(True)):
        print("Thursday")\
        