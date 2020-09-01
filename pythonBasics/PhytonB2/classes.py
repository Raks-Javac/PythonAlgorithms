class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hlo {self.name}! python says hi")


name = input("whats your name? \n")
person1 = Person(name)
person1.talk()

