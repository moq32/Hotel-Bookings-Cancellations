# Predicting and Mitigating Hotel Booking Cancellations

## 🏨 Project Overview
In the hospitality industry, hotel rooms are perishable assets. Cancellations create demand volatility, reduce forecast accuracy, and negatively impact revenue performance. This project leverages real-world Property Management System (PMS) data from two Portuguese hotels—a Resort Hotel (H1) and a City Hotel (H2)—to predict cancellation risks and generate actionable insights for revenue management.

## 📊 Business Impact
- **Historical Loss:** $16.6M (approx. 39.1% of total potential revenue).
- **Forecasted Loss:** $3.68M predicted over the next 6 months.
- **Unit Loss:** Average of $376.71 lost per cancellation.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** * **Data Analysis:** `Pandas`, `NumPy`
    * **Visualization:** `Matplotlib`, `Seaborn`
    * **Machine Learning:** `Scikit-learn`, `XGBoost`
    * **Forecasting:** `Statsmodels` (SARIMAX)

## 📉 Methodology
### 1. Exploratory Data Analysis (EDA)
Identified key cancellation drivers:
* **Lead Time:** Bookings made 181-365 days in advance have the highest risk.
* **Deposit Type:** Non-refundable deposits and Online TA channels show specific cancellation patterns.
* **Seasonality:** Peak risk occurs during summer months.

### 2. Machine Learning & Predictive Modeling
Implemented and compared multiple classification models to predict `is_canceled`:
* **Random Forest:** Primary model for scoring bookings at reservation time.
* **XGBoost & Logistic Regression:** Used for performance benchmarking.

### 3. Time-Series Forecasting
Utilized **SARIMAX** to forecast seasonal booking volumes over a 6-month window to assist in staffing and overbooking strategies.

## 💡 Strategic Recommendations
* **Revenue Management:** Implement daily booking scoring to flag high-risk reservations.
* **Policy Optimization:** Revise deposit policies for Online TA segments and long lead-time bookings.
* **Operations:** Align pricing and staffing levels with SARIMAX volume forecasts.
* **Overbooking:** Use predictive risk scoring to set optimal overbooking levels.