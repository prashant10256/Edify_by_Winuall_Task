def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
number = 5
print("Factorial of", number, "is", factorial(number))
