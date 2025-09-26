# app.py
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# ------------------------------
# Sidebar
# ------------------------------
st.sidebar.title("About This Project")
st.sidebar.info(
    """
    **Stock Market Trend Prediction App**

    This app predicts future stock prices using a **pre-trained LSTM deep learning model**.
    Upload a CSV file with historical stock data to predict the next few days' closing prices.
    """
)

st.sidebar.title("About Me")
st.sidebar.info(
    """
    **Mirza Yasir Abdullah Baig**

    - [LinkedIn](https://www.linkedin.com/in/mirza-yasir-abdullah-baig/)
    - [GitHub](https://github.com/mirzayasirabdullahbaig07)
    - [Kaggle](https://www.kaggle.com/mirzayasirabdullah07)
    """
)

# ------------------------------
# Main Page
# ------------------------------
st.title("📈 Stock Market Trend Prediction - LSTM Model")
st.write("Predict future stock prices for any stock using a pre-trained LSTM model.")

# ------------------------------
# Upload CSV
# ------------------------------
uploaded_file = st.file_uploader("Upload CSV with historical stock data", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("CSV loaded successfully!")
else:
    st.warning("Please upload a CSV file to continue.")
    st.stop()

# ------------------------------
# Show last rows
# ------------------------------
st.subheader("Last 10 rows of the data")
st.write(data.tail(10))

# ------------------------------
# Download button for CSV
# ------------------------------
csv = data.to_csv(index=False)
st.download_button(
    label="📥 Download Stock Data as CSV",
    data=csv,
    file_name="stock_data.csv",
    mime="text/csv"
)

# ------------------------------
# Prepare numeric 'Close' data safely
# ------------------------------
if 'Close' in data.columns:
    close_data = pd.to_numeric(data['Close'], errors='coerce').dropna().values.reshape(-1,1)
elif 'Adj Close' in data.columns:
    close_data = pd.to_numeric(data['Adj Close'], errors='coerce').dropna().values.reshape(-1,1)
else:
    st.error("Could not find a numeric 'Close' column in the CSV.")
    st.stop()

# Historical chart
st.subheader("Historical Closing Price Chart")
st.line_chart(close_data)

# ------------------------------
# Number of days to predict
# ------------------------------
days_to_predict = st.number_input(
    "Enter number of days to predict:",
    min_value=1,
    max_value=30,
    value=5
)

# ------------------------------
# Load LSTM model
# ------------------------------
model = load_model("stock_dl_model.h5")

# ------------------------------
# LSTM Prediction
# ------------------------------
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(close_data)

time_step = 100
if len(scaled_data) < time_step:
    st.error(f"Not enough data to make predictions. Need at least {time_step} rows in CSV.")
else:
    x_input = scaled_data[-time_step:].reshape(1, time_step, 1)
    predicted_prices = []

    for _ in range(days_to_predict):
        pred_price = model.predict(x_input, verbose=0)
        predicted_prices.append(pred_price[0][0])
        pred_price_3d = pred_price.reshape(1,1,1)
        x_input = np.append(x_input[:,1:,:], pred_price_3d, axis=1)

    predicted_prices = scaler.inverse_transform(np.array(predicted_prices).reshape(-1,1))

    st.subheader(f"Predicted Closing Prices for next {days_to_predict} day(s)")
    pred_df = pd.DataFrame({
        'Day': range(1, days_to_predict+1),
        'Predicted Close': predicted_prices.flatten()
    })
    st.write(pred_df)

    # ------------------------------
    # Historical + Predicted Price Chart
    # ------------------------------
    historical_prices = close_data.flatten()
    predicted_prices_flat = predicted_prices.flatten()
    all_prices = np.concatenate([historical_prices, predicted_prices_flat])
    days_hist = np.arange(len(historical_prices))
    days_pred = np.arange(len(historical_prices), len(all_prices))

    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(days_hist, historical_prices, label="Historical Close", color='blue')
    ax.plot(days_pred, predicted_prices_flat, label="Predicted Close", color='red', linestyle='--')
    ax.set_xlabel("Days")
    ax.set_ylabel("Price")
    ax.set_title("Historical + Predicted Closing Prices")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    plt.close(fig)