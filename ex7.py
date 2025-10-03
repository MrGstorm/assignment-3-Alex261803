###############################################################################
#  Program Name  : ex7.py
#  Author         : Alex Sawatsky 
#  Task           : (Write a program that asks the user for their age, 
# if too old it prints you are too old, 
# if young prints you are too young) 
# program also asks for two numbers and prints the larger one 
###############################################################################


age = 17
if age >= 17:
    print("you are too old")
elif age <= 14:
      print("you are too young")

if age == 16:
        print("pefect")
        
num1 = input("enter the first number: ")
num2 = input("enter the second number: ")
# compare 2 numbers and print the larger one 
if num1 > num2:
      print(f"the larger number is: {num1}")
elif num2 > num1:
      print(f"the larger number is: {num2}")
else: 
      print("the two numbers are equal")