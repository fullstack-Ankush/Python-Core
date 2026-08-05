# solution 1

(lambda a : print("It is even") if a%2 == 0 else print("It is odd") )(4) 

# solution 2
fib = lambda n : n if n==0 or n==1 else fib(n-1)+fib(n-2)

print(fib(7))

# solution 3
area = lambda r: 2*3.14*r

print(area(7))

# solution 4

# SOLUTION 5
count = lambda words : print(len(words))

count("Ankush")