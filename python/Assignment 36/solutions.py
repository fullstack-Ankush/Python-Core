# solution 1 print N nturaal number using recursion 

def natural(n):
    if n > 0:
        natural(n - 1)
        print(n, end=' ')


# solution 2  print N nataurala number in reverse using recursion
def natural_reverse(n):
    if n > 0:
        print(n, end=' ')
        natural_reverse(n - 1)

# solution 3  print first N odd natural number using recursion

def odd_natural(n):
    if n > 0:
        odd_natural(n - 1)
        print(2 * n - 1, end=' ')

# solution 4  

def odd_natural_reverse(n):
    if n > 0:
        print(2 * n - 1, end=' ')
        odd_natural_reverse(n - 1)  

# solution 5 print "Ankush" N time using recursion

def print_name(n):
    if n > 0:
        print("Ankush")
        print_name(n - 1)

        

