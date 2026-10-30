height = 7
width = 2 * height + 3

for i in range(height):
    print(("*" * (2 * i + 1)).center(width))

for _ in range(2):
    print("**".center(width))

for _ in range(1):
    print("*" * width)