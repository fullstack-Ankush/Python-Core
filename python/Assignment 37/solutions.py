# solution 1

def even_natural(n):
    if n > 0:
        even_natural(n - 2)
        print( n , end=' ')


even_natural(10)

# solution 2 

def even_natural_reverse(n):
    if n > 0:
        print(n, end=' ')
        even_natural_reverse(n - 2)

# solution 3  print first N sqaure nataural number using recursion

def square_natural(n):
    if n > 0:
        square_natural(n - 1)
        print(n * n, end=' ')

# solution 4 
def cube_natural(n):
    if n > 0:
        cube_natural(n - 1)
        print(n * n * n, end=' ')

# solution 5  print reverse of a give nnumber using recursion

def reverse_number(n):
    if n < 10:
        print(n, end=' ')
    else:
        print(n % 10, end=' ')
        reverse_number(n // 10)



