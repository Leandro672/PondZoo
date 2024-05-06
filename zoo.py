import unittest

class Animal:
    def __init__(self, name, species, happiness_level=50):
        self.name = name
        self.species = species
        self.happiness_level = happiness_level

class Enclosure:
    def __init__(self, species, animals=None):
        self.species = species
        self.animals = animals if animals else []

    def add_animal(self, animal):
        if animal.species == self.species:
            self.animals.append(animal)
        else:
            raise ValueError("Cannot add animal of different species to this enclosure")

class Zoo:
    def __init__(self):
        self.enclosures = []

    def create_enclosure(self, species):
        enclosure = Enclosure(species)
        self.enclosures.append(enclosure)
        return enclosure

    def feed_animal(self, animal, food_quality):
        if food_quality == "good":
            animal.happiness_level += 10
        elif food_quality == "bad":
            animal.happiness_level -= 10

    def attract_visitors(self):
        total_visitors = 0
        for enclosure in self.enclosures:
            for animal in enclosure.animals:
                if animal.happiness_level > 50:
                    total_visitors += 10
                else:
                    total_visitors += 5
        return total_visitors

class TestZoo(unittest.TestCase):
    def test_create_animal(self):
        animal = Animal("Leo", "Lion")
        self.assertEqual(animal.name, "Leo")
        self.assertEqual(animal.species, "Lion")
        self.assertEqual(animal.happiness_level, 50)

    def test_create_enclosure(self):
        zoo = Zoo()
        enclosure = zoo.create_enclosure("Lion")
        self.assertEqual(enclosure.species, "Lion")

    def test_add_animal_to_enclosure(self):
        zoo = Zoo()
        enclosure = zoo.create_enclosure("Lion")
        animal = Animal("Leo", "Lion")
        enclosure.add_animal(animal)
        self.assertEqual(len(enclosure.animals), 1)
        self.assertEqual(enclosure.animals[0].name, "Leo")

    def test_feed_animal(self):
        zoo = Zoo()
        animal = Animal("Leo", "Lion")
        zoo.feed_animal(animal, "good")
        self.assertEqual(animal.happiness_level, 60)

    def test_attract_visitors(self):
        zoo = Zoo()
        enclosure1 = zoo.create_enclosure("Lion")
        enclosure2 = zoo.create_enclosure("Elephant")
        lion = Animal("Leo", "Lion", happiness_level=60)
        elephant = Animal("Ellie", "Elephant", happiness_level=40)
        enclosure1.add_animal(lion)
        enclosure2.add_animal(elephant)
        self.assertEqual(zoo.attract_visitors(), 15)  # Lion enclosure: 10 visitors, Elephant enclosure: 5 visitors

if __name__ == '__main__':
    unittest.main()
