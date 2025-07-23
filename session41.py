# This is a Python script that demonstrates the use of variables and basic data types.
age = 25 
number_of_students = 22  # An integer
price = 19.99            # A float

print("Number of students:", number_of_students)
print("Price of the book:", price)

# Using a string variable
greeting = "Hello, World!"
user_name = 'Alice'

print(greeting)
print("User name:", user_name)

# Using a boolean variable
is_logged_in = True
is_game_over = False

print("Is the user logged in?", is_logged_in)
print("Is the game over?", is_game_over)

# List of favorite colors
favorite_colors = ["red", "green", "blue"]
print("Favorite colors:", favorite_colors)

# Tuple of dimensions
dimensions = (1920, 1080)  # Width and height in pixels
print("Screen dimensions:", dimensions)
# Dictionary of user information
user_info = {
    "name": "Alice",
    "age": 25,
    "is_active": True
}
print("User information:", user_info)

# To Do 
# Variable for your name & age
# List of your favorite foods 
# Dictionary of your pet

sport = {
    "name": "Soccer",
    "players": 11,
    "is_team_sport": True
}

book = {
    "title": "Python Programming",
    "author": "John Doe",
    "published_year": 2021    
}

books = [book, {
    "title": "Learning Python",
    "author": "Jane Smith",
    "published_year": 2020
}]

print("Book 1 Title:", books[0]['title'])
print("Book 2 Title:", books[1]['title'])

user_details = [
    {
        "name": "Alice",
        "age": 25,
        "hobbies": ["reading", "gaming", "hiking"],
        "sport": sport
    },
    {
        "name": "Bob",
        "age": 30,
        "hobbies": ["cooking", "cycling", "photography"],
        "sport": sport
    }
]
print("User 1 : ", user_details[0]['name'])
print("User 2 : ", user_details[1]['name'])

print("User details:")
for user in user_details:
    print(f"Name: {user['name']}, Age: {user['age']}, Hobbies: {', '.join(user['hobbies'])}, Sport: {user['sport']['name']}")
