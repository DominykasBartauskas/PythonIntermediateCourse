from operator import attrgetter


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} is {self.age} years old"


person1 = Person("Jonas", 23)
person2 = Person("Tadas", 31)
person3 = Person("Petras", 60)

list = [person1, person2, person3]

sorted_list_normal = sorted(list, key=attrgetter("name", "age"))
sorted_list_reversed = sorted(list, key=attrgetter("name", "age"), reverse=True)

print(sorted_list_normal)
print(sorted_list_reversed)
