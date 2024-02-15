def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Test
a = 3
b = 7

print("Squares of numbers from", a, "to", b, "are:")
for square in squares(a, b):
    print(square)
