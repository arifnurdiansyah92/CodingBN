class Animal:
  def __init__(self, name):
    self.name = name
    self.__hunger = 5 # Private attribute, 0=full, 10=very hungry

  # A public method to safely interact with the private data
  def feed(self):
    print(f"Feeding {self.name}...")
    self.__hunger = 0 # The only way to change hunger is through this method

  def make_sound(self):
    print(f"{self.name} makes a generic animal sound.")

class Lion(Animal):
  def __init__(self, name):
    # Call the parent's constructor to set up the name
    super().__init__(name)

  # This overrides the parent's make_sound() method
  def make_sound(self):
    print(f"{self.name} lets out a loud ROAR!")

class Zebra(Animal):
  def __init__(self, name):
    super().__init__(name)

  # This also overrides the parent's method with a different behavior
  def make_sound(self):
    print(f"{self.name} makes a happy braying sound.")

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []  # A list to hold animal objects

    def add_animal(self, animal):
        """Adds an animal to the zoo."""
        self.animals.append(animal)
        print(f"{animal.name} has been added to {self.name} Zoo.")
    
    def show_animals(self):
        """Displays all animals in the zoo."""
        print(f"Animals in {self.name} Zoo:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.__class__.__name__})")

    def feed_all(self):
        """Feeds all animals in the zoo."""
        for animal in self.animals:
            animal.feed()
            print(f"{animal.name} has been fed.")

# Create different animal objects
leo = Lion("Leo the Lion")
zara = Zebra("Zara the Zebra")

zoo1 = Zoo("Safari Park")
zoo1.add_animal(leo)
zoo1.add_animal(zara)

zoo2 = Zoo("Wildlife Sanctuary")
zoo2.add_animal(Lion("Simba"))
zoo2.add_animal(Zebra("Marty"))

zoos = [zoo1, zoo2]

for zoo in zoos:
    zoo.show_animals()
    zoo.feed_all()
    print()  # Just for better readability in output