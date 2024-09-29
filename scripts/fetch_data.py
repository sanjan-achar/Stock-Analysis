
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# Alpha Vantage API key (Replace with your API key)
API_KEY = 'GA8D346TW5IHANX2'
ts = TimeSeries(key=API_KEY, output_format='pandas')

# Fetch daily stock data for Tesla ('TSLA')
stock_data, metadata = ts.get_daily(symbol='TSLA', outputsize='full')

# Save the data to a CSV file in the data directory
csv_filename = '../data/tesla_stock_data.csv'
stock_data.to_csv(csv_filename)
print(f"Stock data saved to '{csv_filename}'")
