#!/usr/bin/env python3
#The line above is included to run the program in the terminal without reusing python3
#run 
#chmod +x Reverse_String.py
#./Reverse_String.py

#this is the test code snippet where I reverse a string that the user has entered
def reverse_Operation(user_str):
    user_str_rev = ""
    if user_str != "":
        for i in user_str[::-1]:
            user_str_rev+=i
        return user_str_rev
    else:
        return "You have entered an empty string."
    
user_str = input("Enter anything<< ")
print(reverse_Operation(user_str))



