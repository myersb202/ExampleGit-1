class Animal:
    tricks = []
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
    def addTrick(self, trick):
        self.tricks.append(trick)
        

lion = Animal('lion')
cat = Animal('cat')
cat.display()
lion.display()
lion.addTrick('trip you')
cat.addTrick('purr')
print('End')
