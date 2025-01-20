# Ask user for their name
name=input("what's your name? ").capitalize()


# function is like an actio or verb that lets you don something in the program.  In this case "print" is a fucntion.
#"()" in the parathesis you put arguments 
# Return values , 
# Variables store  value(container for a some value) 
# "str"= string which is a type of data

#split user name into first name and last name 
first,last =name.split(" ")
# say hello to user
print(f"Hello,{first}")

#int numbers,