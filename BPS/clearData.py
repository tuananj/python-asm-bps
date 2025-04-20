# import pandas as pd

# # Define file paths
# customer_file = 'customer_table.csv'
# market_trend_file = 'market_trend.csv'
# product_detail_file = 'product_detail.csv'
# product_group_file = 'product_group.csv'
# sale_file = 'sale_table.csv'
# supplier_file = 'supplier_table.csv'

# # Load data into DataFrames
# customer_df = pd.read_csv(customer_file)
# market_trend_df = pd.read_csv(market_trend_file)
# product_detail_df = pd.read_csv(product_detail_file)
# product_group_df = pd.read_csv(product_group_file)
# sale_df = pd.read_csv(sale_file)
# supplier_df = pd.read_csv(supplier_file)

# # Cleaning Customer Table
# customer_df['ContactEmail'] = customer_df['ContactEmail'].fillna('not_provided@example.com')
# customer_df['CustomerID'] = customer_df['CustomerID'].astype(int)
# customer_df['PostalCode'] = customer_df['PostalCode'].astype(str)

# # Cleaning Market Trend Table
# market_trend_df['TrendID'] = market_trend_df['TrendID'].astype(int)
# market_trend_df['StartDate'] = pd.to_datetime(market_trend_df['StartDate'])
# market_trend_df['EndDate'] = pd.to_datetime(market_trend_df['EndDate'])

# # Cleaning Product Detail Table
# product_detail_df['ProductID'] = product_detail_df['ProductID'].astype(int)
# product_detail_df['Price'] = product_detail_df['Price'].astype(float)
# product_detail_df['StockQuantity'] = product_detail_df['StockQuantity'].astype(int)
# product_detail_df['SupplierID'] = product_detail_df['SupplierID'].astype(int)

# # Cleaning Product Group Table
# # Check for non-numeric values in ProductGroupID before converting
# invalid_product_group_ids = product_group_df[pd.to_numeric(product_group_df['ProductGroupID'], errors='coerce').isna()]
# if not invalid_product_group_ids.empty:
#     print("Found invalid ProductGroupID values:")
#     print(invalid_product_group_ids)
#     # Optionally, handle these rows, for example, by dropping them or converting them to a default value
#     # product_group_df = product_group_df.drop(invalid_product_group_ids.index)

# product_group_df['ProductGroupID'] = pd.to_numeric(product_group_df['ProductGroupID'], errors='coerce').fillna(0).astype(int)

# # Cleaning Sale Table
# sale_df.dropna(subset=['CustomerID', 'ProductID'], inplace=True)
# sale_df['SaleID'] = sale_df['SaleID'].astype(int)
# sale_df['CustomerID'] = sale_df['CustomerID'].astype(int)
# sale_df['ProductID'] = sale_df['ProductID'].astype(int)
# sale_df['Quantity'] = sale_df['Quantity'].astype(int)
# sale_df['TotalAmount'] = sale_df['TotalAmount'].astype(float)
# sale_df['SaleDate'] = pd.to_datetime(sale_df['SaleDate'])

# # Cleaning Supplier Table
# supplier_df['SupplierID'] = supplier_df['SupplierID'].astype(int)
# supplier_df['ZipCode'] = supplier_df['ZipCode'].astype(str)

# # Save cleaned data to new CSV files
# customer_df.to_csv('cleaned_customer_table.csv', index=False)
# market_trend_df.to_csv('cleaned_market_trend.csv', index=False)
# product_detail_df.to_csv('cleaned_product_detail.csv', index=False)
# product_group_df.to_csv('cleaned_product_group.csv', index=False)
# sale_df.to_csv('cleaned_sale_table.csv', index=False)
# supplier_df.to_csv('cleaned_supplier_table.csv', index=False)

# print("Data cleaning completed and saved to new CSV files.")
