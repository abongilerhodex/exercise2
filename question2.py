# Question 2: Comparison and Logical Operators

a = float(input("Enter A value: "))
b = float(input("Enter B value: "))
c = float(input("Enter C value: "))

if a>b :
  print("A is greater than B.")
elif a<=b :
  print("A is not greater than B.")


if b % 2 == 0:
    print("B is even.")
else:
    print("B is odd.")

if c<=a :
    print("C is not greater than A.")
else: 
   print("C is greater than A.")

# Final condition
if a>b or b % 2 == 0 and c<=a :
   print("True")
else: 
   print("False")
