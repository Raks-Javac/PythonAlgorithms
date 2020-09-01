name = input("What is your name ? \n")

if len(name) < 3:
    print("name must be at least three characters")
elif len(name) > 50:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good")

