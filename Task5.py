def factorial(num):
    result = 1
    for i in range (1 , num + 1):
        result *= i
    return result

num = int(input("Enter a Number: "));
print("Factorial of", num, "is", factorial(num));




