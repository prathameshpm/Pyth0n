"""
print("#")
print("#")
print("#")
"""

"""
for _ in range(3):
    print("#")
"""

"""
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()
"""

"""
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()
"""

"""
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
"""


def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
main()