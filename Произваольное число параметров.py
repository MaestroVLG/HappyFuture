def custom_print(*args, **kwargs):
    print("Напишите позиционный аргумент:")
    for arg in args:
        print(arg)
    print("\nНапишите позиционный аргумент:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

if __name__ == "__main__":
    custom_print(3, "welcome", False, x=20, y="world", z=True)
    result = recursive_factorial(6)
    print("\nFactorial of 6 is:", result)