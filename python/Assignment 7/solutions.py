#solution 1

a = 5
b = bin(8)
print(a,b)

#solution 2
x = 0b1011
print(x)

#solution 3
hex_string = "1A"

# Step 1: Convert hex string to base-10 integer
decimal_value = int(hex_string, 16)

# Step 2: Convert integer to octal string
octal_string = oct(decimal_value)

print(octal_string)  # Output: 0o32

#solution 4
octal  = '27'
decimal = int(octal,8)
binary = bin(decimal)
print(binary)

#solution 5
a = '25'
b = '39'

x = int(a,8)
y = int(b , 16)
z = x + y
result = bin(z)
print(result)
