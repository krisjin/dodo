class Person:
    def __init__(self):
        print("init")

    def hello(self,name):
        self.name = name
        print("hello " +self.name)


p = Person()
p.hello("kris")