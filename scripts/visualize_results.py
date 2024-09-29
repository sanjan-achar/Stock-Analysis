import pandas as pd
import matplotlib.pyplot as plt

# Load actual stock prices
stock_data = pd.read_csv('../data/cleaned_tesla_stock_data.csv', parse_dates=['date'])
stock_data.set_index('date', inplace=True)

# Load predicted prices (for example, from LSTM)
predicted_data = pd.read_csv('../data/predicted_prices.csv', parse_dates=['date'])
predicted_data.set_index('date', inplace=True)

# Plot actual vs predicted prices
plt.figure(figsize=(10, 5))
plt.plot(stock_data['4. close'], label='Actual Prices', color='blue')
plt.plot(predicted_data['Predicted Prices'], label='Predicted Prices (LSTM)', color='orange', linestyle='--')
plt.axvline(x=stock_data.index[-1], color='red', linestyle='--')  # Mark the prediction point
plt.title('Actual vs Predicted Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()