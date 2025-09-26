# 📈 Stock Market Trend Prediction App

An **AI-powered web application** built with **Streamlit** that predicts **future stock prices** using a **Long Short-Term Memory (LSTM) deep learning model** trained on historical market data.  

---

## 🚀 Demo
🔗 [Live App on Streamlit](https://stockmarketprediction07.streamlit.app/)  

---

## 📌 Features
- Predicts **future stock closing prices** using an **LSTM model**.  
- User-friendly **Streamlit interface**.  
- Upload a CSV file with historical stock data.  
- Generates predictions for **1–30 days ahead**.  
- Provides interactive **charts for historical + predicted prices**.  
- Includes an **About Me** sidebar with portfolio links.  

---

## 🔍 Usage
1. Open the app in your browser.  
2. Upload a CSV file containing **historical stock data**.  
   - Must contain a column: `Close` (or `Adj Close`).  
3. Choose the **number of days** you want predictions for.  
4. Click **Predict**.  
5. Get results:  
   - 📊 Table of predicted prices.  
   - 📈 Graph combining **historical + predicted trends**.  

---

## 📊 Dataset
The app works with **stock market historical data**.  

- You can fetch stock data using **Yahoo Finance API (`yfinance`)** or download from any trusted source.  
- Columns required:  
  - `Date`  
  - `Open`  
  - `High`  
  - `Low`  
  - `Close` or `Adj Close`  
  - `Volume`  

---

## ⚙️ Tech Stack
- **Python 3.9+**  
- **Streamlit** (Frontend Web App)  
- **NumPy & Pandas** (Data Processing)  
- **Matplotlib & Plotly** (Visualizations)  
- **Scikit-learn** (Preprocessing & Scaling)  
- **TensorFlow / Keras** (LSTM Deep Learning Model)  

---

## 📸 Screenshots
### 🏠 Home Page
<img width="1894" height="848" alt="image" src="https://github.com/user-attachments/assets/8946b8d2-67d2-4e74-a9b1-2121a49e6841" />

### 📊 Prediction Results
<img width="1873" height="810" alt="image" src="https://github.com/user-attachments/assets/fd394daa-ce85-4dc3-85fc-1bb544de6b05" />

### 📊 Prediction Results
<img width="1883" height="793" alt="image" src="https://github.com/user-attachments/assets/d63a5aa6-2f35-4d0a-b35d-3f6b20a1e959" />

### 📊 Prediction Results
<img width="1902" height="840" alt="image" src="https://github.com/user-attachments/assets/8ee22954-3939-4756-b74e-2032802db329" />


---

## 👨‍💻 Author
**Mirza Yasir Abdullah Baig**  

- 🌐 [Kaggle](https://www.kaggle.com/mirzayasirabdullah07)  
- 💼 [LinkedIn](https://www.linkedin.com/in/mirza-yasir-abdullah-baig/)  
- 💻 [GitHub](https://github.com/mirzayasirabdullahbaig07)  

---

## ❤️ Acknowledgements
- [Yahoo Finance API (`yfinance`)](https://pypi.org/project/yfinance/)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Scikit-learn](https://scikit-learn.org/stable/)  
- [TensorFlow/Keras](https://www.tensorflow.org/)  

---

## ⚠️ Disclaimer
This project is for **educational and research purposes only** and should **NOT** be considered as financial advice. Always do your own research before investing in the stock market.  

---
