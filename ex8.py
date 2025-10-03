###############################################################################
#  Program Name   : ex8.py
#  Author         : Alex Sawatsky 
#  Task           : (Write a loop that prints the numbers 1-5. 
# Also ask for the password, 
# if correct you are gifted access, if not try again.)
# When finished it will print hello 5 times 
###############################################################################

count = 1 
while count <= 5:
    print (count)
    count +=1

password = ""
while password != "tiger123":
    password = input("enter password: ")
    print("access granted")

while True:
    word = input("type stop to end: ")
    if word == "stop":
        break 
#initialize a counter variable 
count = 0
#while loop to print "hello" five times 
while count <= 5:
    print("Hello")
    count+=1 #increment the counter 