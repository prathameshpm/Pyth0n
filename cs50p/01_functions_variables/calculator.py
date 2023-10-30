"""

x = 1
y = 2

z = x + y

print(z)

"""
"""

x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)

"""
"""

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

"""
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

"""
"""

print(int(input("What's x? ")) + int(input("What's y? ")))

"""
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

"""
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)

"""
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")

"""
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)

"""
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)

"""
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")

"""
"""

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

"""

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n ** 2

main()