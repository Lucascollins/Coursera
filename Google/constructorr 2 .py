class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return f"This apple is {self.color} and its flavor is {self.flavor}"

jonagold = Apple("red ","sweet")
print(jonagold)


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(some_person.name)

# Create a new instance with a name of your choice
some_person = Person("Lucas")
# Call the greeting method
print(some_person)
