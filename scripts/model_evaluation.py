import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the cleaned stock data
csv_filename = '../data/cleaned_tesla_stock_data.csv'
stock_data = pd.read_csv(csv_filename, parse_dates=['date'])

# Load the predictions
predictions = pd.read_csv('../data/predicted_prices.csv', parse_dates=['date'])
predictions.set_index('date', inplace=True)

# Ensure both actual and predicted values are aligned
actual_values = stock_data.set_index('date')['4. close'][-30:]  # Last 30 actual values

# Calculate evaluation metrics
mae = mean_absolute_error(actual_values, predictions)
mse = mean_squared_error(actual_values, predictions)
rmse = mean_squared_error(actual_values, predictions, squared=False)  # Root Mean Squared Error

# Print evaluation results
print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'Root Mean Squared Error (RMSE): {rmse}')

# Plot actual vs predicted values
plt.figure(figsize=(10, 5))
plt.plot(actual_values.index, actual_values, label='Actual Closing Prices', color='blue')
plt.plot(predictions.index, predictions['Predicted Prices'], label='Predicted Prices', color='orange', linestyle='--')

# Title and labels
plt.title('Actual vs Predicted Tesla Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.grid(True)
plt.tight_layout()  # Adjust layout for better fit
plt.show()