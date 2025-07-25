import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Slide 2: The Study Case Data ---
# This is our consistent data source for all the examples.
game_data = {
    'Title': ['Stardew Valley', 'Red Dead 2', 'Cyberpunk 2077', 'Elden Ring', 'Baldur\'s Gate 3'],
    'Genre': ['Simulation', 'Action-Adventure', 'RPG', 'Action RPG', 'RPG'],
    'Year': [2016, 2018, 2020, 2022, 2023],
    'Hours Played': [300, 120, 80, 200, 250]
}
df = pd.DataFrame(game_data)

print("--- Our Game Collection DataFrame ---")
print(df)
print("\nNow generating plots...")

# --- Slide 3: The Line Plot (The Time Machine) ---
print("Displaying Line Plot...")
# Note: We sort by 'Year' to make the line connect logically from oldest to newest.
df_sorted = df.sort_values(by='Year')
plt.figure(figsize=(8, 5)) # Create a new figure for each plot
plt.plot(df_sorted['Year'], df_sorted['Hours Played'], marker='o', linestyle='--')
plt.title("Hours Played by Year of Release")
plt.xlabel("Year Released")
plt.ylabel("Hours Played")
plt.grid(True)
plt.show()


# --- Slide 4: The Bar Chart (The Showdown) ---
print("Displaying Bar Chart...")
plt.figure(figsize=(10, 6)) # Create a new figure
sns.barplot(x='Title', y='Hours Played', data=df)
plt.title("Comparison of Hours Played per Game")
plt.xlabel("Game Title")
plt.ylabel("Hours Played")
plt.xticks(rotation=45, ha='right') # Rotate labels for better readability
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()


# --- Slide 5: The Histogram (The Group Photo) ---
print("Displaying Histogram...")
plt.figure(figsize=(8, 5)) # Create a new figure
sns.histplot(df['Hours Played'], bins=3, kde=True)
plt.title("Distribution of Hours Played")
plt.xlabel("Hours Played Bins")
plt.ylabel("Number of Games (Frequency)")
plt.show()


# --- Slide 6: The Scatter Plot (The Detective's Clue Board) ---
print("Displaying Scatter Plot...")
plt.figure(figsize=(8, 5)) # Create a new figure
sns.scatterplot(x='Year', y='Hours Played', data=df, s=100) # s=100 makes the dots bigger
plt.title("Relationship Between Release Year and Hours Played")
plt.xlabel("Year Released")
plt.ylabel("Hours Played")
plt.grid(True)
plt.show()


# --- Slide 7: The Heatmap (The Treasure Map) ---
print("Displaying Heatmap...")
# For this example, we'll add a 'Rating' column to our data to make the heatmap more interesting.
df['User Rating'] = [9.6, 9.7, 7.5, 9.5, 9.9]

# Create a correlation matrix of the numerical columns.
# .corr() calculates how strongly variables are related to each other.
correlation_matrix = df[['Year', 'Hours Played', 'User Rating']].corr()

plt.figure(figsize=(8, 6)) # Create a new figure
# annot=True shows the correlation numbers on the map.
# cmap='coolwarm' is a color scheme that makes it easy to see positive (warm) and negative (cool) correlations.
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Game Data")
plt.show()

print("\nAll plots have been displayed.")
