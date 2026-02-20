# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:
# Date:

print("--- Factorial Finder ---\n")


# Write your code here
def factorial(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
number = int(input("Enter number: "))
fact = factorial(number)
if fact is False:
    print(f"Factorial of {number} is not defined.")
    
else:
    print(f"Factorial of {number} is {fact}.")
