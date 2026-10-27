# Question 4: Combining Operators and Conditionals

num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))

plus = "+"
minus = "-"
multiply = "*"
divide = "/"

num_add = (num1 + num2)
num_minus = (num1 - num2)
num_mult = (num1 * num2)

operation = input("Enter operation: ")

if operation == minus:
  print(num_minus)
elif operation == plus:
   print(num_add)
elif operation == multiply:
  print(num_mult)
elif num2 == 0:
   print("Cannot divide by zero!")
else:
   print(num1 / num2)
