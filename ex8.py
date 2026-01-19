###############################################################################
#  Program Name   : ex8.py
#  Author         : Alex Sawatsky 
#  Task           : (Write a loop that prints the numbers 1-5. Also ask for the password, 
# if correct you are gifted access, if not try again.)
# When finished it will print hello 5 times 
###############################################################################

while True:
    # get input from user 
    word = input("Enter a word(type 'exit' to quit): ")

    # check if user wants to exit
    if word.lower() == 'exit':
        print("Exiting the program.")
        break

    # otherwise continue 
    print(f"You entered: {word}")


 