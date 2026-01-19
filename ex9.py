###############################################################################
#  Program Name   : ex9.py
#  Author         : Alex Sawatsky 
#  Task           : (prints odd numbers from 1-19 and print tiger on 5 seperate lines)
###############################################################################


# Iterate through every number from 1 up to but not including 20
for i in range (1, 20):
    # The % (modulus) operator gives the remainder of division
    # If the number divided by 2 has a remainder of 1, it is odd
    if i % 2 == 1:
        print(i)
