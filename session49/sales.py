import pandas as pd
import matplotlib.pyplot as plt

def find_and_visualize_peak_sale(filename="sales.csv"):
    """
    Reads the sales CSV, finds the single best sales day, prints the result,
    and then creates a chart to visualize all the data.
    """
    # Step 1: Read the CSV file into a pandas DataFrame
    try:
        sales_df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        print("Please make sure the CSV file is in the same directory or provide the correct path.")
        return

    # Step 2: Convert the 'Date' column to a proper datetime format
    sales_df['Date'] = pd.to_datetime(sales_df['Date'])

    # --- This is the new part that answers the question ---
    # Step 3: Find the row with the maximum sales value
    highest_sale_row = sales_df.loc[sales_df['Sales'].idxmax()]
    
    # Extract the specific date and sales amount
    peak_date = highest_sale_row['Date'].strftime('%Y-%m-%d') # Format date for readability
    peak_sales = highest_sale_row['Sales']

    print("--- Answering the question from the data ---")
    print(f"The highest sales amount was ${peak_sales:,.2f}.")
    print(f"It happened on: {peak_date}")
    print("\nNow, let's visualize this...")
    # ----------------------------------------------------

    # Step 4: Create the visualization
    plt.figure(figsize=(14, 7))
    plt.plot(sales_df['Date'], sales_df['Sales'], label='Daily Sales', color='dodgerblue')

    # Highlight the peak sale on the chart
    plt.plot(pd.to_datetime(peak_date), peak_sales, 'ro', markersize=10, label=f'Highest Sale: ${peak_sales:,.2f}')

    # Step 5: Customize the plot
    plt.title('Daily Sales Performance Over 500 Days', fontsize=18, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sales (USD)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.gcf().autofmt_xdate()

    # Step 6: Display the final chart
    plt.tight_layout()
    plt.show()

# --- Run the analysis and visualization ---
# Make sure 'sales_data_500.csv' is in the same folder as this script
find_and_visualize_peak_sale()
