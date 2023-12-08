import pandas as pd
import glob
import os

# The directory where your CSV files are stored
csv_directory = '/Users/jerryli/Downloads/archive/Most important coins'

# The pattern to match your CSV files, assuming they have a .csv extension
csv_pattern = os.path.join(csv_directory, '*.csv')

# Define the date range
start_date = '2014-09-18'
end_date = '2023-04-11'

# Get a list of all CSV files in the directory
csv_files = glob.glob(csv_pattern)

# List to hold dataframes
dfs = []

# Loop over the list of csv files
for file in csv_files:
    
    # Read the CSV file and parse the 'Date' column as a date
    df = pd.read_csv(file, parse_dates=['Date'])
    
    # Filter the dataframe for the given date range
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df = df.loc[mask]

    # Fill NaN values with zero
    df.fillna(0, inplace=True)
    
    # Extract a unique identifier from the filename, e.g., the coin name
    unique_identifier = os.path.basename(file).split('.')[0]
    
    # Rename columns to include the unique identifier, skipping 'Date'
    df.rename(columns=lambda x: f"{unique_identifier}_{x}" if x != 'Date' else x, inplace=True)
    
    # Set the 'Date' column as the index
    df.set_index('Date', inplace=True)
    
    # Append the filtered dataframe to the list
    dfs.append(df)

# Concatenate all dataframes on the 'Date' index
merged_df = pd.concat(dfs, axis=1, join='outer')

# Reset the index so that 'Date' becomes a regular column again
merged_df.reset_index(inplace=True)

# Save the merged dataframe to a new CSV file
merged_output = os.path.join(csv_directory, 'merged_data.csv')
merged_df.to_csv(merged_output, index=False)

print(f'Merged CSV saved to {merged_output}')
