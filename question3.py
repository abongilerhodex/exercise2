# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = float(input("Enter test score: "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if score>= 90 :
  print("Grade: A ")
elif score>= 80 :
  print("Grade: B ")
elif score>= 70 :
  print("Grade: C ")
elif score>= 60 :
  print("Grade: D ")
else:
  print("Grade: F ")
# TODO: Print the grade for the given score