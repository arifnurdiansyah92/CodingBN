class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  # This is a method
  def bark(self):
    print(f"{self.name} says: Woof!")
    
# Use the Dog blueprint to create two different Dog objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Each dog has its own data
print(f"{dog1.name} is {dog1.age} years old.") # Output: Buddy is 3 years old.
print(f"{dog2.name} is {dog2.age} years old.") # Output: Lucy is 5 years old.

# And they can perform the same actions
dog1.bark() # Output: Buddy says: Woof!
dog2.bark() # Output: Lucy says: Woof!