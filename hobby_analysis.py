import pandas as pd
import numpy as np

def analyze_game_collection():
    """
    This function runs the complete analysis for our video game collection.
    """
    # Step 1 & 2: Define the data and create the DataFrame
    game_collection_data = {
        'Title': ['The Witcher 3', 'Elden Ring', 'Stardew Valley', 'Cyberpunk 2077', 'Baldur\'s Gate 3', 'Red Dead Redemption 2'],
        'Platform': ['PC', 'PC', 'PC', 'PS5', 'PC', 'PS5'],
        'Genre': ['RPG', 'Action RPG', 'Simulation', 'RPG', 'RPG', 'Action-Adventure'],
        'Hours Played': [150, 200, 300, 80, 250, 120]
    }
    df = pd.DataFrame(game_collection_data)
    
    print("--- My Game Collection DataFrame ---")
    print(df)
    print("\n" + "="*40 + "\n") # Separator for clarity

    # Step 3: Answering the Questions
    print("--- Answering Our Questions ---")

    # Question 1 (Level 1): What is the average number of hours played?
    avg_hours = df['Hours Played'].mean()
    print(f"1. The average hours played across all games is: {avg_hours:.2f} hours.")

    # Question 2 (Level 2): Which games are on the 'PC' platform?
    pc_games = df[df['Platform'] == 'PC']
    print("\n2. The following games are on PC:")
    print(pc_games[['Title', 'Genre']]) # Show only relevant columns

    # Question 3 (Level 3 - NumPy Challenge): Add a 'Days Played' column
    # Convert 'Hours Played' to a NumPy array for calculation
    hours_array = np.array(df['Hours Played'])
    # Calculate days played (assuming 24 hours per day)
    days_played_array = hours_array / 24
    # Add the new column to the DataFrame
    df['Days Played'] = days_played_array
    
    print("\n3. Added a new 'Days Played' column using NumPy.")
    print("   (Note: This is a raw calculation and not literal days of play!)")
    
    print("\n" + "="*40 + "\n")

    # Display the final, updated DataFrame
    print("--- Final DataFrame with New Column ---")
    # We use .round(2) to make the new column easier to read
    print(df.round(2))


# --- Run the entire analysis ---
analyze_game_collection()
