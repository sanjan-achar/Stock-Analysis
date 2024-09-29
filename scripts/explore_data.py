
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data from the CSV file
csv_filename = '../data/tesla_stock_data.csv'
stock_data = pd.read_csv(csv_filename)

# Convert the 'date' column to datetime format
stock_data['date'] = pd.to_datetime(stock_data['date'])

# Plot the closing price over time
plt.figure(figsize=(10, 5))
plt.plot(stock_data['date'], stock_data['4. close'], label='Closing Price')
plt.title('Tesla Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()
