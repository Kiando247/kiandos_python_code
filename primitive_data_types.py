#primitive data types
#Subscripting
#print("Hello"[0])

#Integer = whole number
#print(430 + 431)

#Large integers
#print(960_302_781)

#Float = Floating Point Number(because the decimal point can "float" to any part of the number)
#print(3.14159)
#type checking
#print(type(3.14159))

#Boolean
#print(True)
#print(False)

# name = input("Enter your name:\n ")
# print(len(name))
# print(type(name))

# print(type("Hello World"))
# print(type(2026))
# print(type(True))
# print(type(3.14159))

#typeconversion/typecasting
# first_number = int("123")
# second_number = int("456")
# print(first_number + second_number)

# int("132")
# float()
# str()
# bool()
# tuple()

#print(f"Number of letters in your name:  + len(input("Enter your name"))")
# Solution:
#len(input("Enter your name") can be divided into:
# user_name = input("Enter your name: ") # str
# length_of_username = len (user_name) # converting the string to a number

#now we have two statements:
# print(type("Number of letters in your name: ")) # will give str, and:
# print(type(length_of_username)) # will give int
#Concatenation cannot occur among strings and integers,
# so we use typecasting:
# i.e print(str(length_of_username))
# hence solution:

# print("Number of letters in your name: " + str(length_of_username))

# N.B: Cheat code(fstring) is
# print(f"number of letters: {length_of_username}")

