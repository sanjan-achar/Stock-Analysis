import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data from the CSV file (raw data fetched from fetch_data.py)
csv_filename = '../data/tesla_stock_data.csv'
stock_data = pd.read_csv(csv_filename)

# Set the date as the index and ensure the frequency is set
stock_data['date'] = pd.to_datetime(stock_data['date'])
stock_data.set_index('date', inplace=True)

# Set the frequency to daily
stock_data = stock_data.asfreq('D')

# Check for missing values in '4. close' column
print("Missing values in '4. close':", stock_data['4. close'].isnull().sum())

# Fill missing values if any
if stock_data['4. close'].isnull().sum() > 0:
    stock_data['4. close'] = stock_data['4. close'].ffill()  # Forward fill

# After handling missing values, check again
print("Missing values in '4. close' after handling:", stock_data['4. close'].isnull().sum())

# Fill missing values for all relevant columns
stock_data.fillna(method='ffill', inplace=True)  # Forward fill for all columns

# After handling missing values, check again
print("Total missing values in DataFrame after handling:\n", stock_data.isnull().sum())

# Save the cleaned dataset
cleaned_csv_filename = '../data/cleaned_tesla_stock_data.csv'
stock_data.reset_index(inplace=True)  # Ensure the index (date) is included as a column
stock_data.to_csv(cleaned_csv_filename, index=False)  # Save with date column
print(f"Cleaned data saved to '{cleaned_csv_filename}'")