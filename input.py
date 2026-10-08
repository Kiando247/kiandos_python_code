


#print(len(input("What is your name? ")))


while True:
    name = input("What is your name? ").split().ttitle()
    if name: # Checks if the string is not empty
        break
    print("Please enter a valid name.")

# 2. Greet the user using an f-string
print(f"Hello {name}!")

# Count characters while ignoring internal spaces
letters_only = name.replace(" ", "")
print(f"Your name has {len(letters_only)} characters.") 

