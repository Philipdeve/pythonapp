import re

txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

#x = re.split("\s", txt) #the /s stands for whitespace

x = re.sub("\s", "9", txt)

print(x)

#creating  a  python program that checks the validity of a password:

# passwordInput = input("Input your password: ")

# if (len(passwordInput) < 6 ):
#     print("password length should be above 6 Characters")
# elif  re.search("[a-z]", passwordInput) and re.search("[A-Z]", passwordInput) and  re.search("[0-9]", passwordInput) and re.search("[$#@]", passwordInput) and not re.search("\s", passwordInput) : 
#     print("valid password")
# else:
#     print("invalid Password")


# Write a Python program that matches a word at the beginning of a string.

def textMatch(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
            return 'Found a match!'
        else:
            return('Not matched!')

print(textMatch("The boy  ran home."))
print(textMatch("@## The boy ran home"))



 