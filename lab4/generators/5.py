def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test
n = 5

print("Counting down from", n, "to 0:")
for number in countdown(n):
    print(number)
