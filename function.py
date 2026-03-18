# function with return value
# used when we want to send result back
def add(a , b):
    return a + b
result = add(2 , 3)
print(result)

# Task 1 : create a function to calculate and return result

    
# task 2 : create a function to check if number is even or odd
# def check_even_odd( num ):
#     if num % 2 == 0 :
#         return "Even"
#     else :
#         return "Odd"
# check_even_odd(2)

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a digit: "))
print("The number is:", check_even_odd(num))

# task 3 : create a function to find the factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))

# task 4 : create a function to find max between 3 numbers
def max( a, b, c):
    if a >= b and a >= c :
        return a
    elif b >= a and b >= c :
        return b
    else :
        return c
    
a = float(input("Enter first number :"))
b = float(input("Enter second number :"))
c = float(input("Enter third number :"))
result = max( a, b, c)
print("Maximum of numbers :",result)     

# task 5 : create a function to check a string is a palindrome 
# or not
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input_str = input("Enter a string :")
result = is_palindrome(input_str)
if result :
    print(f"{ input_str} is a palindrome")
else :
    print(f"{input_str} is not a palindrome")

# task 6 : create a function to find area of circle 
def area_of_circle(radius):
    return 3.14 * radius ** 2

radius = float(input("Enter radius of the circle:"))
area = area_of_circle(radius)
print(f"The area of the circle is : {area}")
