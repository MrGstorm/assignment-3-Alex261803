###############################################################################
#  Program Name   : ex10.py
#  Author         : Alex Sawatsky 
#  Task           : (Get three friends names and store them in a list then 
# print them)
###############################################################################

friends = []
for i in range(3):
    friend_name = input("Enter your friend's name: ")
    friends.append(friend_name)

print("Your friends are:")
for name in friends:
    print(name)