# Working with inputs
name = input("Whats your name : \n ")
greetings = f"Hlo  { name} ! how you doing ? "
print(greetings)

# converting your inputs to specific datatypes like int or floats
print("Welcome to the basic Arithmetic Calculator")

# num1 and num2 to integer
# num1 =int( input("Input first number"))
# num2 = int(input("input Second number"))

# num1 and num2 in floats
num1 =float(input("Input first number \n"))
num2 = float(input("input Second number \n"))
sumer = [num1,num2]
print( "The sum is " + str(sum(sumer)))
print( "The substration  is " + str((num1-num2)))
print( "The modulus is  is " + str((num1%num2)))
print( "The division is " + str((num1/num2)))
print( "The multiplication  is " + str((num1*num2)))



