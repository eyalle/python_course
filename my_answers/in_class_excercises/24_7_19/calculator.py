class Calculator:
    last = ""

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def display(self):
        print('here are the current details:')
        print(f'A = {self.a}, B = {self.b}')
        print(f'latest result is {self.last}\n')

    def add(self):
        Calculator.last = self.a + self.b
        self.display()

    def sub(self):
        Calculator.last = self.a - self.b
        self.display()

if __name__ == "__main__":
    calc1 = Calculator(1, 2)
    calc1.display()
    calc1.add()
    calc1.sub()

    calc2 = Calculator(3, 4)
    calc2.display()
    calc2.add()

    calc1.display()