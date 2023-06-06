#!/usr/bin/env python3
#The line above is included to run the program in the terminal without reusing python3
#run 
#chmod +x Reverse_String.py
#./Reverse_String.py

#this is the test code snippet where I reverse a string that the user has entered
def reverse_Operation(user_str):
    user_str_rev = ""
    if user_str == "" or user_str == " ":
        raise ValueError("You have entered an empty string or a string without content.")
    else:
        for i in user_str[::-1]:
            user_str_rev+=i
        return user_str_rev
    
user_str = input("Enter anything<< ")
print(reverse_Operation(user_str))




