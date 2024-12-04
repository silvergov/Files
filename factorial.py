"""
Create a function that calculates the factorial of a number.
n! = n * (n-1).(n-2).(n-3)* ..... * 2 * 1
The factorial of zero is 1. 1!=1.
"""
def factorial(x):
    n = 1
    for i in range(2, x+1):
        n = n * i
    return n

def main():
    x = input("What is the number you want the factorial of? ")
    x = int(x)                  # change string input to integer 
    result = factorial(x)       # calculate factorial
    print("The factorial of " + str(x) + " is " + str(result))

main()