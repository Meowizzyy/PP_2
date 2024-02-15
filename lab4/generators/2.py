def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    n = int(input("Enter a number (n): "))
    even_numbers = even_numbers_generator(n)
    print("Even numbers between 0 and", n, "are:", end=" ")
    print(*even_numbers, sep=", ")

main()
