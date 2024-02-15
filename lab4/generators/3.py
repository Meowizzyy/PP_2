def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
def main():
    n = int(input("Enter a number (n): "))
    numbers = divisible_by_3_and_4_generator(n)
    print("Numbers between 0 and", n, "divisible by both 3 and 4 are:")
    for number in numbers:
        print(number)

main()
