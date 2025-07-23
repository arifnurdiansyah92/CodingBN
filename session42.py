enrolled = True

if enrolled:
    print('Welcome to Coding BN')
else:
    print(':(')

# Fruit List
fruit_list = ["apple", "banana", "cherry"]
print(fruit_list[0], fruit_list[1], fruit_list[2])

# Using a loop to print each fruit
for fruit in fruit_list:
    print(fruit)

# 1. DEFINE the recipe
def greet(name):
  print(f"Hello, {name}!")

# 2. CALL it anytime you want!
greet("Arif")
greet("World")

def validate_and_greet_user():
  """
  Asks for a username, validates its length, and greets the user.
  """
  username = input("Please enter your username: ")
  
  # Check the length of the username string
  if 3 <= len(username) <= 10:
    # If valid, greet them
    print(f"Welcome, {username}! It's great to see you.")
  elif len(username) < 3:
    # If too short, inform them
    print("Sorry, that username is too short. It must be at least 3 characters.")
  else:
    # If too long, inform them
    print("Sorry, that username is too long. It cannot exceed 10 characters.")

# Run the function
validate_and_greet_user()

def check_even_odd():
    """
    Asks the user for a number and checks if it's even or odd.
    """
    try:
        number = int(input("Please enter a number: "))
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    except ValueError:
        print("That's not a valid number. Please enter an integer.")

# Run the function
check_even_odd()

i = 0
while i < 5:
    print(i + 1)
    i += 1 

for i in range(5):
    print(i + 1)

for i in [1,2,3,4,5]:
    print(i)