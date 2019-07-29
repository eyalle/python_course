class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_name(self):
        print(f'Hello! my name is {self.name} and I\'m {self.age} years old\n')

if __name__ == "__main__":
    user1 = Person("Eyal", 31)
    user2 = Person("Idan", 28)

    user1.print_name()
    user2.print_name()
    user2.age = 27
    user2.print_name()