"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(df):
    # Define the columns to be split
    columns_to_split = ['FG', '3PT', 'FT']
    
    for col in columns_to_split:
        if col in df.columns:
            # Split the column into makes and attempts
            makes_attempts = df[col].str.split('-', expand=True)
            df[f'{col}M'] = pd.to_numeric(makes_attempts[0], errors='coerce')  # Makes
            df[f'{col}A'] = pd.to_numeric(makes_attempts[1], errors='coerce')  # Attempts
            
            # Remove the original column
            df.drop(columns=[col], inplace=True)
    
    return df

def main():
    """Creates the data frame and view and starts the app."""
    try:
        frame = pd.read_csv("cleanbrogdonstats.csv")
        print("CSV file loaded successfully.")
        frame = cleanStats(frame)  # Clean the data before passing it to the view
        print("Data cleaned successfully.")
        print(frame.head())  # Print the first few rows of the DataFrame for verification
        HoopStatsView(frame)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
