import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Tải dữ liệu từ CSV
sale_df = pd.read_csv('cleaned_sale_table.csv')

# Chọn các cột sử dụng cho mô hình
X = sale_df[['Quantity']]  # Biến độc lập
y = sale_df['TotalAmount']  # Biến phụ thuộc

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Tính toán các chỉ số hiệu suất
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Biểu đồ phân tán và đường hồi quy
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.title('Actual vs Predicted Total Amount')
plt.legend()
plt.show()

# Biểu đồ phân phối phần dư (Residual Plot)
plt.figure(figsize=(10, 6))
residuals = y_test - y_pred
plt.scatter(y_pred, residuals, color='green', alpha=0.5)
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel('Predicted Total Amount')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.show()

# Biểu đồ so sánh giá trị thực tế và dự đoán (Actual vs. Predicted Plot)
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, color='blue', label='Actual')
plt.scatter(range(len(y_pred)), y_pred, color='red', label='Predicted', alpha=0.5)
plt.xlabel('Index')
plt.ylabel('Total Amount')
plt.title('Actual vs Predicted Total Amount')
plt.legend()
plt.show()

# Biểu đồ đường thời gian cho dự đoán (Time Series Plot)
# Đảm bảo rằng sale_df có cột 'Date' và được chuyển đổi sang định dạng datetime
if 'Date' in sale_df.columns:
    sale_df['Date'] = pd.to_datetime(sale_df['Date'])
    
    # Sắp xếp dữ liệu theo ngày để biểu đồ có ý nghĩa
    sale_df = sale_df.sort_values('Date')
    
    plt.figure(figsize=(14, 7))
    plt.plot(sale_df['Date'], sale_df['TotalAmount'], color='blue', label='Actual')
    
    # Dự đoán doanh số theo ngày
    # Chúng ta cần dự đoán cho các ngày trong dữ liệu
    future_dates = pd.date_range(start=sale_df['Date'].max(), periods=10, freq='D')
    future_X = np.linspace(X['Quantity'].min(), X['Quantity'].max(), len(future_dates)).reshape(-1, 1)
    future_sales = model.predict(future_X)
    
    plt.plot(future_dates, future_sales, color='red', linestyle='--', label='Predicted')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    plt.title('Time Series Plot of Actual and Predicted Total Amount')
    plt.legend()
    plt.show()
