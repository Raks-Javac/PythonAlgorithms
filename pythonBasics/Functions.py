# Working with functions

# functions without parameters or arguements

def greetings():
    print("Hello World ! Greetings from the no arguemental function")

greetings()


# functions with parameters
# greetings bot

def greeting_robot(name,age):
     
    print("Hello "+name+"!" +" you are " +age+ " years old right ?")
    
    

greeting_robot(name = input("Whats your name ? \n").upper(),
    age = input("How old are you ? \n"))
   


