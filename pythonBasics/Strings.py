# Lesson 3
# Working with Strings

phrase = "Raks Javac"

# returns a capitalized type of the first character of your variable
print(phrase.capitalize())

# return the whole of your string to be upper case
print(phrase.upper())
# makes the whole of your character lowercase
print(phrase.lower())

# checks if your string is uppercase and returns a boolean value(either true or false)
print(phrase.isupper())

# returns the character in the index 
index = 3
print(phrase[0])
print(phrase[index])

# returns where the string position (in number) starts from
print(phrase.index("Javac"))

# replaces the whole string

print(phrase.replace("Javac","FLutter\nPython"))
print(phrase)