# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
plus = "+"
minus = "-"
multiply = "*"
divide = "/"
num_add = (num1 + num2)
num_minus = (num1 - num2)
num_mult = (num1 * num2)
num_div = (num1 / num2)

operation = input("Enter operation: ")


# TODO: Use conditional statements to perform the chosen operation on num1 and num2

if operation == minus:
  print(num_minus)
elif operation == multiply:
  print(num_mult)
else:
  print(num_add)





# TODO: Handle the case of division by zero


# TODO: Print the result of the operation