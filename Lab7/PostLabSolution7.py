# PE #5 // breadprice.py

import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(file_path):
    try:
        df = pd.read_csv(file_path)
        monthly_cols = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        if not all(col in df.columns for col in monthly_cols):
            print("Error: Not all monthly price columns (Jan-Dec) found in the CSV.")
            return pd.DataFrame()

        df_melted = df.melt(id_vars=['Year'], value_vars=monthly_cols, var_name='Month', value_name='Price')

        df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce').astype('Int64')

        df_melted['Price'] = pd.to_numeric(df_melted['Price'], errors='coerce')

        df_melted.dropna(subset=['Year', 'Price'], inplace=True)

        return df_melted
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred during data loading and cleaning: {e}")
        return pd.DataFrame()

def plot_average_price_per_year(df, output_filename="average_bread_price_per_year.png"):
    if df.empty:
        print("No data to plot.")
        return

    average_price_yearly = df.groupby('Year')['Price'].mean().reset_index()

    average_price_yearly = average_price_yearly.sort_values('Year')

    plt.figure(figsize=(10, 6))
    plt.plot(average_price_yearly['Year'], average_price_yearly['Price'], marker='o', linestyle='-')
    plt.title('Average Bread Price Per Year')
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(output_filename)
    print(f"Plot saved to {output_filename}")

if __name__ == "__main__":
    file_path = "breadprice.csv"
    cleaned_df = load_and_clean_data(file_path)

    if not cleaned_df.empty:
        plot_average_price_per_year(cleaned_df)
    else:
        print("Could not process data due to errors or empty DataFrame.")

--------------------------------------------------

# PE #6 // hoopsstatsapp.py (modified)

"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(df):
    """
    Cleans the basketball statistics DataFrame by splitting 'FG', '3PT',
    and 'FT' columns into made (M) and attempted (A) components,
    and converting them to numeric types.

    Args:
        df (pd.DataFrame): The raw DataFrame loaded from the CSV.

    Returns:
        pd.DataFrame: The cleaned DataFrame with split numeric columns.
    """
    cleaned_df = df.copy() # Work on a copy to avoid modifying the original DataFrame directly

    for col in ['FG', '3PT', 'FT']:
        if col in cleaned_df.columns:
            # 1. Convert the column to string type to ensure .str accessor works
            # 2. Split the string by '/' into two new temporary columns
            #    expand=True creates new columns from the list
            split_data = cleaned_df[col].astype(str).str.split('/', expand=True)

            # Check if splitting was successful (i.e., produced two columns)
            if split_data is not None and split_data.shape[1] == 2:
                # Assign to new 'M' (Made) and 'A' (Attempted) columns
                # Convert these new columns to numeric (float is generally safer for stats)
                cleaned_df[col + 'M'] = pd.to_numeric(split_data[0], errors='coerce')
                cleaned_df[col + 'A'] = pd.to_numeric(split_data[1], errors='coerce')

                # Drop the original combined column
                cleaned_df = cleaned_df.drop(col, axis=1)
            else:
                print(f"Warning: Could not split column '{col}'. It might not contain 'X/Y' format for all rows or is missing. Keeping original column.")
                # If split fails, ensure the original column is still numeric if possible
                cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors='coerce')
        else:
            print(f"Warning: Column '{col}' not found in DataFrame.")
            
    # Fill any NaNs that might result from conversion or splitting errors with 0
    # This is a common practice for numeric stats where NaN implies zero contribution.
    cleaned_df = cleaned_df.fillna(0)

    print("DataFrame cleaned successfully by splitting FG/3PT/FT and converting to numeric.")
    return cleaned_df

def main():
    """Creates the data frame and view and starts the app."""
    file_path = "cleanbrogdonstats.csv"
    frame = None # Initialize frame to None

    try:
        frame = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please make sure it's in the same directory.")
        return # Exit if file not found
    except Exception as e:
        print(f"An error occurred while loading the CSV file: {e}")
        return # Exit on other loading errors

    if frame is not None:
        cleaned_frame = cleanStats(frame)
        # Pass the *cleaned* frame to the HoopStatsView constructor
        HoopStatsView(cleaned_frame)
    else:
        print("DataFrame could not be loaded or processed.")

if __name__ == "__main__":
    main()
