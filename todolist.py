# A list to store our tasks
todo_list = ["Read a chapter of a book", "Write some Python code", "Go for a walk"]

def show_tasks():
  """
  Iterates through the to-do list and prints each task with its number.
  """
  print("\n--- Your To-Do List ---")
  # A 'for' loop to go through each item with its index
  for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")
  print("----------------------")

def add_task():
  """
  Asks the user for a new task and adds it to the list.
  """
  new_task = input("What task would you like to add? ")
  todo_list.append(new_task) # .append() is a method to add to a list
  print(f"'{new_task}' has been added to your list!")

def remove_task():
    """
    Asks the user for a task number to remove and removes it from the list.
    """
    try:
        task_number_to_remove = int(input("What task number would you like to remove? "))
        if 1 <= task_number_to_remove <= len(todo_list):
            removed_task = todo_list.pop(task_number_to_remove - 1) # .pop() removes by index
            print(f"'{removed_task}' has been removed from your list!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\n1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")
    action = input("Select Menu: ")
    return action

# --- Main Program ---
while True:
   action = show_menu()
   if action == "1":
       add_task()
   elif action == "2":
       show_tasks()
       remove_task()
   elif action == "3":
       show_tasks()
   elif action == "4":
       break
   else:
       print("Invalid option. Please try again.")