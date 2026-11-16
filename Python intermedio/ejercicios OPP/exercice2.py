class Bus:
    

    def __init__(self,max_passengers):

        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        
        if len(self.passengers) >= self.max_passengers:
            print("bus is full")

        else:
            self.passengers.append(person)

    def remove_passenger(self,person):

            if person in self.passengers:

                self.passengers.remove(person)
            else:
                print(f"this {person} is not on the bus")


class Person:

    def __init__(self,name):
        self.name = name



person1 = Person('carlos')
person2 = Person('ana')
person3 = Person('pedro')

my_bus = Bus(2)

my_bus.add_passenger(person1)
my_bus.add_passenger(person2)
my_bus.add_passenger(person3)

print(f'this bus has {len(my_bus.passengers)} passengers')

my_bus.remove_passenger(person1)
print(len(my_bus.passengers))

my_bus.remove_passenger(person3)


for person in my_bus.passengers:
    print(person.name)