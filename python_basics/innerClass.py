class outer:
    def __init__(self):
        self.name="Outer Class"
    class inner:
        def __init__(self):
            self.name="Inner Class"
        def display(self):
            return "This is the "+ self.name
Outer=outer()
print(Outer.name)  # Accessing outer class attribute
Inner=outer.inner()
print(Inner.name)  # Accessing inner class attribute
print(Inner.display())  # Calling method of inner class
