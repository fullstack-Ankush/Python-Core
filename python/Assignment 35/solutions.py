# solution 1 (print LCM of 2 numbers)
def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

# solution 2 count words in  string
def countWords(s):
    return len(s.split())   


# solution 3  crete a list of prime number between 2 number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

