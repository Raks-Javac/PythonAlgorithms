import modules
from modules import greet
from determinaer import max_min
import random 


print(random.choice([1,2,3,2]))
modules.greet("Jack")
greet("jack")
max_min()

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print(f"({dice1},{dice2})")