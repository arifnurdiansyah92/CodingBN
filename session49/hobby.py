import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- The Data Source ---
# This is the data provided in the challenge.
game_collection_data = {
    'Title': ['The Witcher 3', 'Elden Ring', 'Stardew Valley', 'Cyberpunk 2077', 'Baldur\'s Gate 3', 'Red Dead Redemption 2'],
    'Platform': ['PC', 'PC', 'PC', 'PS5', 'PC', 'PS5'],
    'Genre': ['RPG', 'Action RPG', 'Simulation', 'RPG', 'RPG', 'Action-Adventure'],
    'Hours Played': [150, 200, 300, 80, 250, 120]
}

df = pd.DataFrame(game_collection_data)

# --- Part 1: The Matplotlib Mission Solution ---
print("--- Creating visualization with Matplotlib ---")

# Get the game titles for the x-axis from the DataFrame
titles = df['Title']
# Get the hours played for the y-axis from the DataFrame
hours = df['Hours Played']

# Create a bar chart using plt.bar()
plt.bar(titles, hours, color='skyblue') # Added color for customization

# Add a title to the plot
plt.title("Hours Played per Game (Matplotlib)")

# Add a label for the X-axis
plt.xlabel("Game Title")

# Add a label for the Y-axis
plt.ylabel("Hours Played")

# This makes the x-axis labels easier to read by rotating them
plt.xticks(rotation=45, ha='right') 
# Adjusts plot to prevent labels from overlapping
plt.tight_layout() 

# Show the plot
plt.show()


# --- Part 2: The Seaborn Mission Solution ---
print("\n--- Creating the same visualization with Seaborn ---")

# Create a bar chart using sns.barplot().
# Seaborn handles the axes and data mapping elegantly.
sns.barplot(x='Title', y='Hours Played', data=df)

# Add a title to the plot
plt.title("Hours Played per Game (Seaborn)")

# This makes the x-axis labels easier to read
plt.xticks(rotation=45, ha='right')
# Adjusts plot to prevent labels from overlapping
plt.tight_layout() 

# Show the plot
plt.show()

# --- Bonus Challenge 2: A Different Story ---
print("\n--- Bonus Challenge: Genre Count ---")

# Use Seaborn's countplot to easily visualize categorical data
sns.countplot(x='Genre', data=df, palette='viridis')

plt.title("Count of Games per Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Games")

plt.tight_layout()
plt.show()
