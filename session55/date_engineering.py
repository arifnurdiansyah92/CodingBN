import pandas as pd

# Our starting ingredient: a list of dates
df = pd.DataFrame({'sale_date': ['2023-01-01', '2023-01-02', '2023-01-03']})

# First, we make sure Pandas understands it's a date
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Now, the magic! We create new features (ingredients).
df['day_of_week'] = df['sale_date'].dt.day_name()
df['month'] = df['sale_date'].dt.month

print(df)