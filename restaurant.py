class MenuItem:
    """
    The base class for any item on the restaurant menu.
    Encapsulates the core details of a menu item.
    """
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        # Encapsulation: Calories are private and cannot be changed directly.
        self.__calories = calories

    def get_calories(self):
        """A public method to safely access the private calorie count."""
        return self.__calories

    def display(self):
        """Polymorphism: This is the base display method."""
        print(f"{self.name} - ${self.price:.2f} ({self.get_calories()} cal)")

class FoodItem(MenuItem):
    """
    Inheritance: A specific type of MenuItem for food.
    It inherits all properties and methods from MenuItem.
    """
    def __init__(self, name, price, calories, is_vegetarian):
        # Call the parent's constructor to set up the base properties
        super().__init__(name, price, calories)
        self.is_vegetarian = is_vegetarian

    def display(self):
        """
        Polymorphism: Overrides the parent's display method
        to add food-specific details.
        """
        vegetarian_status = " (V)" if self.is_vegetarian else ""
        base_info = f"{self.name}{vegetarian_status} - ${self.price:.2f} ({self.get_calories()} cal)"
        print(base_info)

class DrinkItem(MenuItem):
    """
    Inheritance: A specific type of MenuItem for drinks.
    """
    def __init__(self, name, price, calories, volume_ml):
        super().__init__(name, price, calories)
        self.volume_ml = volume_ml

    def display(self):
        """
        Polymorphism: Overrides the parent's display method
        to add drink-specific details.
        """
        base_info = f"{self.name} ({self.volume_ml}ml) - ${self.price:.2f} ({self.get_calories()} cal)"
        print(base_info)

class Restaurant:
    """A manager class to hold and manage the menu."""
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item_to_menu(self, item):
        """Adds a MenuItem object to the menu list."""
        if isinstance(item, MenuItem):
            self.menu.append(item)
        else:
            print("Error: Only MenuItem objects can be added to the menu.")

    def remove_item_from_menu(self, item_name):
        """Finds an item by name and removes it from the menu."""
        item_to_remove = None
        for item in self.menu:
            if item.name.lower() == item_name.lower():
                item_to_remove = item
                break
        
        if item_to_remove:
            self.menu.remove(item_to_remove)
            print(f"'{item_to_remove.name}' has been removed from the menu.")
        else:
            print(f"Error: Item '{item_name}' not found on the menu.")

    def display_menu(self):
        """Displays the entire restaurant menu."""
        print(f"\n--- Menu for {self.name} ---")
        if not self.menu:
            print("The menu is currently empty.")
        else:
            for item in self.menu:
                item.display()
        print("------------------------" + "-" * len(self.name))

def main():
    """The main function to run the interactive program."""
    my_restaurant = Restaurant("The OOP Cafe")

    # Populate with initial items
    my_restaurant.add_item_to_menu(FoodItem("Classic Burger", 12.50, 750, False))
    my_restaurant.add_item_to_menu(FoodItem("Veggie Wrap", 9.00, 450, True))
    my_restaurant.add_item_to_menu(DrinkItem("Cola", 2.50, 140, 330))
    my_restaurant.add_item_to_menu(DrinkItem("Orange Juice", 3.00, 120, 250))

    while True:
        print("\nRestaurant Management System")
        print("1. Display Menu")
        print("2. Add New Item")
        print("3. Remove Item")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            my_restaurant.display_menu()
        elif choice == '2':
            print("What type of item to add?")
            item_type = input(" (food/drink): ").lower()
            name = input("Enter item name: ")
            try:
                price = float(input("Enter price: "))
                calories = int(input("Enter calories: "))

                if item_type == 'food':
                    is_veg_input = input("Is it vegetarian? (yes/no): ").lower()
                    is_veg = is_veg_input == 'yes'
                    new_item = FoodItem(name, price, calories, is_veg)
                    my_restaurant.add_item_to_menu(new_item)
                elif item_type == 'drink':
                    volume = int(input("Enter volume in ml: "))
                    new_item = DrinkItem(name, price, calories, volume)
                    my_restaurant.add_item_to_menu(new_item)
                else:
                    print("Invalid item type.")
                print(f"'{name}' added to the menu.")
            except ValueError:
                print("Invalid input. Price, calories, and volume must be numbers.")

        elif choice == '3':
            item_name_to_remove = input("Enter the name of the item to remove: ")
            my_restaurant.remove_item_from_menu(item_name_to_remove)
        
        elif choice == '4':
            print("Exiting system. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

main()
