import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Load the cleaned stock data
stock_data = pd.read_csv('../data/cleaned_tesla_stock_data.csv', parse_dates=['date'])
stock_data.set_index('date', inplace=True)

# Use the '4. close' as the feature and target (for demonstration purposes)
X = stock_data.index.factorize()[0].reshape(-1, 1)  # Convert dates to numerical format
Y = stock_data['4. close'].values

# Split data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions
predictions = model.predict(X_test)

# Calculate RMSE for performance evaluation
rmse = mean_squared_error(Y_test, predictions, squared=False)
print(f'RMSE for Linear Regression: {rmse}')

# Save the model to disk
with open('../Models/linear_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)