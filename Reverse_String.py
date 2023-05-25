#this is the test code snippet where I reverse a string that the user has entered

user_str = input("Enter anything<< ")
def reverse_Operation(user_str):
    user_str_rev = ""
    if user_str != "":
        for i in user_str[::-1]:
            user_str_rev+=i
        print(user_str_rev)
    else:
        print("You have entered an empty string.")



