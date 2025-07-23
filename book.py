class Book:
    """
    Represents a book with a title, author, pages, and reading progress.
    """
    # Step 2: Define the __init__ Constructor with properties
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1  # A default property
        # Bonus Challenge property
        self.bookmarks_placed = 0

    # Step 3, Method 1: Changes a property (self.current_page)
    def read_page(self):
        """Increments the current page, simulating reading."""
        if self.current_page < self.pages:
            self.current_page += 1
            print(f"You are now on page {self.current_page} of '{self.title}'.")
        else:
            print(f"You have finished reading '{self.title}'!")

    # Step 3, Method 2: Performs an action
    def get_summary(self):
        """Prints a summary of the book's details."""
        print("--- Book Summary ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Pages: {self.pages}")
        print(f"Currently on page: {self.current_page}")
        print(f"Bookmarks placed: {self.bookmarks_placed}")
        print("--------------------")

    # Bonus Challenge Method
    def place_bookmark(self):
        """Adds a bookmark and increments the transaction counter."""
        self.bookmarks_placed += 1
        print(f"Bookmark placed on page {self.current_page}. You now have {self.bookmarks_placed} bookmark(s).")


# Step 4: Create at least two objects (instances)
print("Creating two book objects...")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Dune", "Frank Herbert", 412)

# --- Test the methods for the first book ---
print("\n--- Interacting with Book 1: The Hobbit ---")
book1.get_summary()
book1.read_page()
book1.read_page()
book1.place_bookmark()
book1.get_summary()


# --- Test the methods for the second book ---
print("\n--- Interacting with Book 2: Dune ---")
book2.get_summary()
book2.place_bookmark()
book2.place_bookmark()
book2.get_summary()
