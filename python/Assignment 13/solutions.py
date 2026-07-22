#solution 1
a = input("Enter a number ")
if(len(a) == 3):
    print("Yes, it is a 3-digit number ")
else:
    print("No , not a 3-digit number ")

#solution 2
b = 3
if( b>0):
    print("Positive")
elif (b<0):
    print("Negative")
else:
    print("zero")


#solution 3
a ,b = 5,2
if(a>0 and b>0):
    print("real and distinct roots")
elif(a==0 and b==0):
    print("real and equal roots")
else:
    print("imaginary roots")


#solution 5
a = 5
b = 5
c = 5

if(a>b and a>c):
    print(a,"is greater")
elif(b>a and b>c):
    print(b,"is greater")
elif (c>a and c>b):
    print(c,"is greater")
else:
    print("All are equal")


