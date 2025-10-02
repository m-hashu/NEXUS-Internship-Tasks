# Task 6 – Sales Forecasting (Time Series Analysis)

## 📌 Objective
Forecast daily sales for the next 30 days to help with inventory planning.

## 📊 Key Steps
- Aggregated Superstore dataset into daily sales.
- Checked stationarity using ADF test.
- Built SARIMA(1,1,1)(1,1,1,7) model.
- Forecasted next 30 days of sales.

## 📈 Metrics
- MAE: ~979
- RMSE: ~1316
- MAPE: ~2103% (inflated due to zero/small sales days)

## 🛠️ Tools Used
- Python
- statsmodels (SARIMAX)
- scikit-learn (metrics)

## ✅ Outcome
SARIMA model captured sales trends well, producing actionable forecasts for inventory management.
