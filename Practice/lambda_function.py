# A lambda function in Python is a small, anonymous function defined using the lambda keyword. 
# It can take any number of arguments but can only have one expression.

# Example 1: Adding two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Example 2: Squaring a number
square = lambda x: x**2
print(square(4))  # Output: 16

# Example 3: Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 4: Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Example 5: Lambda with conditional expression
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even_odd(7))  # Output: Odd
print(check_even_odd(4))  # Output: Even