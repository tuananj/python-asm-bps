# import pandas as pd
# import matplotlib.pyplot as plt
# # Đảm bảo rằng các đường dẫn đến file CSV là chính xác
# customer_df = pd.read_csv('cleaned_customer_table.csv')
# market_trend_df = pd.read_csv('cleaned_market_trend.csv')
# product_detail_df = pd.read_csv('cleaned_product_detail.csv')
# product_group_df = pd.read_csv('cleaned_product_group.csv')
# sale_df = pd.read_csv('cleaned_sale_table.csv')
# supplier_df = pd.read_csv('cleaned_supplier_table.csv')

# # product_group_count = product_detail_df['Category'].value_counts()
# # plt.figure(figsize=(8, 8))
# # plt.pie(product_group_count, labels=product_group_count.index, autopct='%1.1f%%', startangle=140)
# # plt.title('Distribute products by group')
# # plt.show()


# top_products = product_detail_df.sort_values(by='StockQuantity', ascending=False).head(10)
# plt.figure(figsize=(10, 6))
# plt.bar(top_products['ProductName'], top_products['StockQuantity'], color='skyblue')
# plt.xticks(rotation=45, ha='right')
# plt.xlabel('Name Product')
# plt.ylabel('Quantity in stock')
# plt.title('Top 10 products with highest stock quantity')
# plt.show()


# sale_df['SaleDate'] = pd.to_datetime(sale_df['SaleDate'])
# sales_over_time = sale_df.groupby(sale_df['SaleDate'].dt.to_period('M')).size()
# sales_over_time.index = sales_over_time.index.to_timestamp()
# plt.figure(figsize=(12, 6))
# plt.plot(sales_over_time.index, sales_over_time.values, marker='o', linestyle='-', color='green')
# plt.xlabel('Time')
# plt.ylabel('Sales volume')
# plt.title('Sales trends over time')
# plt.show()


# sales_by_product = sale_df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False).head(10)
# sales_by_product.index = sales_by_product.index.map(lambda x: product_detail_df.loc[product_detail_df['ProductID'] == x, 'ProductName'].values[0])
# plt.figure(figsize=(10, 6))
# sales_by_product.plot(kind='bar', color='orange')
# plt.xlabel('Name Product')
# plt.ylabel('Sales quantity')
# plt.title('Top 10 best selling products')
# plt.xticks(rotation=45, ha='right')
# plt.show()


# plt.figure(figsize=(10, 6))
# product_detail_df.boxplot(column='Price', by='Category', grid=False)
# plt.xlabel('Product Group')
# plt.ylabel('Product price')
# plt.title('Product price distribution by group')
# plt.suptitle('')
# plt.show()


# # Aggregating total sales by customer
# sales_by_customer = sale_df.groupby('CustomerID')['TotalAmount'].sum()

# # Merging with customer details to get customer names
# sales_by_customer = sales_by_customer.reset_index()
# sales_by_customer = sales_by_customer.merge(customer_df[['CustomerID', 'CustomerName']], on='CustomerID')

# # Plotting the pie chart
# plt.figure(figsize=(10, 10))
# plt.pie(sales_by_customer['TotalAmount'], labels=sales_by_customer['CustomerName'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(sales_by_customer))))
# plt.title('Sales Distribution by Customer')
# plt.show()

# # Aggregating sales quantity by product
# sales_quantity_by_product = sale_df.groupby('ProductID')['Quantity'].sum()
# sales_quantity_by_product = sales_quantity_by_product.reset_index()
# sales_quantity_by_product = sales_quantity_by_product.merge(product_detail_df[['ProductID', 'StockQuantity']], on='ProductID')

# # Plotting the scatter plot
# plt.figure(figsize=(10, 6))
# plt.scatter(sales_quantity_by_product['StockQuantity'], sales_quantity_by_product['Quantity'], alpha=0.6, edgecolors='w', linewidth=0.5)
# plt.xlabel('Stock Quantity')
# plt.ylabel('Sales Quantity')
# plt.title('Product Stock vs. Sales Quantity')
# plt.grid(True)
# plt.show()

# # Aggregating product counts by category
# category_distribution = product_detail_df['Category'].value_counts()

# # Plotting the pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(category_distribution, labels=category_distribution.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(category_distribution))))
# plt.title('Product Distribution by Category')
# plt.show()
