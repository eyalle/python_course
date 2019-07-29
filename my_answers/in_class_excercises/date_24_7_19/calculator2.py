from calculator import Calculator

class Calculator2(Calculator):
    last_results = []
    
    def display(self):
        print(f'here are the current details:\tA = {self.a}, B = {self.b}')
        print(f'latest results are: {Calculator2.last_results}\n')        

    def add(self):
        Calculator2.last_results.append(self.a + self.b)
        self.display()

    def sub(self):
        Calculator2.last_results.append(self.a - self.b)
        self.display()

    def multi(self):
        Calculator2.last_results.append(self.a * self.b)
        self.display()

if __name__ == "__main__":
    calc1 = Calculator2(1, 2)
    calc2 = Calculator2(3, 4)
    calc3 = Calculator2(5, 6)

    calc1.add()
    calc2.sub()
    calc3.multi()