import pandas as pd

# --- 1. Data Collection & Feature Selection ---
try:
    # Read the 'gym_attendance.csv' file into a DataFrame.
    df = pd.read_csv('gym_attendance.csv')
except FileNotFoundError:
    print("Error: 'gym_attendance.csv' not found.")
    print("Please make sure the CSV file is in the same folder as your script.")
    exit()

# For this analysis, we don't need 'member_id' or 'gender'.
# Create a new DataFrame called 'df_selected' that only contains the
# 'check_in_timestamp' and 'membership_type' columns.
features_to_select = ['check_in_timestamp', 'membership_type']
df_selected = df[features_to_select]


# --- 2. Feature Engineering (The Creative Part) ---
# Convert the 'check_in_timestamp' column to a datetime object first.
df_selected['check_in_timestamp'] = pd.to_datetime(df_selected['check_in_timestamp'])

# Create a new 'day_of_week' column.
# Use the .dt.day_name() attribute on the timestamp column.
df_selected['day_of_week'] = df_selected['check_in_timestamp'].dt.day_name()

# Create a new 'hour_of_day' column to help with the next step.
# Use the .dt.hour attribute.
df_selected['hour_of_day'] = df_selected['check_in_timestamp'].dt.hour

# Create the 'time_session' column using a helper function and .apply().
def get_session(hour):
  """Categorizes an hour into a time session."""
  if 5 <= hour < 12:
    return 'Morning'
  elif 12 <= hour < 17:
    return 'Afternoon'
  else:
    return 'Night'

df_selected['time_session'] = df_selected['hour_of_day'].apply(get_session)

print("--- Data After Feature Engineering ---")
print(df_selected.head())


# --- 3. Analysis with GroupBy ---
print("\n--- Gym Attendance Analysis ---")
# Find the busiest day of the week.
# .value_counts() is a convenient way to group by a category and count the occurrences.
busiest_day = df_selected['day_of_week'].value_counts()
print("\nAttendance by Day of the Week:")
print(busiest_day)

# Find the most popular time session.
busiest_session = df_selected['time_session'].value_counts()
print("\nAttendance by Time Session:")
print(busiest_session)


# --- 4. Advanced Analysis with Pivot Tables ---
print("\n--- Peak Times by Membership Type ---")
# Create a pivot table to see how many check-ins each membership type
# has during each time session.
# We use 'day_of_week' as the value to count, but any column would work.
pivot = df_selected.pivot_table(index='time_session', columns='membership_type', values='day_of_week', aggfunc='count')

# Fill any missing combinations with 0 for better readability
pivot = pivot.fillna(0)

print(pivot)

print("\n--- Mission Complete! ---")
