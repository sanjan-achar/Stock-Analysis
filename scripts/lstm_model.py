import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Input
import matplotlib.pyplot as plt

# Load the cleaned stock data
stock_data = pd.read_csv('../data/cleaned_tesla_stock_data.csv', parse_dates=['date'])
stock_data.set_index('date', inplace=True)

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(stock_data['4. close'].values.reshape(-1, 1))

# Prepare data for LSTM
def create_dataset(data, time_step=1):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i + time_step), 0]
        X.append(a)
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 60  # Number of previous days to use for predicting the next day
X, Y = create_dataset(scaled_data, time_step)

# Reshape X to be [samples, time steps, features] for LSTM
X = X.reshape(X.shape[0], X.shape[1], 1)

# Build and configure the LSTM model
model = Sequential()
model.add(Input(shape=(X.shape[1], 1)))  # Input layer
model.add(LSTM(50, return_sequences=True))
model.add(Dropout(0.2))  # Regularization to prevent overfitting
model.add(LSTM(50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(25))
model.add(Dense(1))  # Output layer

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, Y, batch_size=1, epochs=10)

# Prepare the last 60 days of data for prediction
last_60_days = scaled_data[-time_step:]  # Take the last 60 days
last_60_days = last_60_days.reshape(1, time_step, 1)

# Predict the next day
predicted_price = model.predict(last_60_days)
predicted_price = scaler.inverse_transform(predicted_price)  # Rescale to original values
print(f'Predicted price for the next day: {predicted_price[0][0]}')

# Save the model in the new format
model.save('../Models/lstm_stock_model.keras')