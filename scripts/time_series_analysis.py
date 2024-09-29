import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load the cleaned stock data
csv_filename = '../data/cleaned_tesla_stock_data.csv'
stock_data = pd.read_csv(csv_filename)

# Print column names for debugging
print("Column names in DataFrame:", stock_data.columns)

# Ensure 'date' is parsed correctly and set as index
if 'date' in stock_data.columns:
    stock_data['date'] = pd.to_datetime(stock_data['date'])
    stock_data.set_index('date', inplace=True)
else:
    print("The 'date' column does not exist in the DataFrame.")

# Set the frequency to daily
stock_data = stock_data.asfreq('D')

# Check for missing values in '4. close' column
print("Missing values in '4. close':", stock_data['4. close'].isnull().sum())

# Fill missing values if any
if stock_data['4. close'].isnull().sum() > 0:
    stock_data['4. close'] = stock_data['4. close'].ffill()  # Forward fill

# After handling missing values, check again
print("Missing values in '4. close' after handling:", stock_data['4. close'].isnull().sum())

# Plot the data to inspect it visually
plt.figure(figsize=(10, 5))
plt.plot(stock_data['4. close'], label='Closing Price')
plt.title('Tesla Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Step 1: Time Series Decomposition
if stock_data['4. close'].isnull().sum() == 0:
    try:
        decomposition = seasonal_decompose(stock_data['4. close'], model='additive')
        decomposition.plot()
        plt.show()
    except ValueError as e:
        print("Error during decomposition:", e)
else:
    print("Still missing values in '4. close' after handling.")

# Step 2: Stationarity Test
result = adfuller(stock_data['4. close'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# Step 3: Build a Baseline Forecasting Model
model = ExponentialSmoothing(stock_data['4. close'], trend='add', seasonal=None)
model_fit = model.fit()
predictions = model_fit.forecast(steps=30)  # Forecast for the next 30 days

# After generating predictions in time_series_analysis.py
predictions = pd.DataFrame(predictions, columns=['Predicted Prices'])
# Create a date range for the predictions
predictions.index = pd.date_range(start=stock_data.index[-1] + pd.Timedelta(days=1), periods=30)
predictions.index.name = 'date'  # Ensure the index is named 'date'

# Save predictions to a CSV file
predictions.to_csv('../data/predicted_prices.csv')

# Plot the actual vs. predicted values
plt.figure(figsize=(10, 5))
plt.plot(stock_data['4. close'], label='Actual Closing Prices')
plt.plot(predictions_df.index, predictions_df['Predicted Prices'], label='Predicted Prices', linestyle='--')
plt.title('Tesla Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

