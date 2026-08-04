class Test:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"

t1 = Test("Alice",38)
print(t1.__dict__)