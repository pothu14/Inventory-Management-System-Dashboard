import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("inventory_mock_dataset_v2.csv")

# --- KPIs ---
total_value = df['Total_Value'].sum()
in_stock_count = df[df['In_Stock'] == 'Yes'].shape[0]
print(f"Total Inventory Value: ₹{total_value:,.2f}")
print(f"In-Stock Products Count: {in_stock_count}")

# --- Category-wise Stock (Bar Chart) ---
category_stock = df.groupby('Category')['Quantity_Purchased'].sum()
category_stock.plot(kind='bar', title='Stock by Category', ylabel='Quantity', xlabel='Category')
plt.tight_layout()
plt.show()

# --- Purchase Trend (Line Chart) ---
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
purchase_trend = df.groupby('Purchase_Date')['Quantity_Purchased'].sum()
purchase_trend.plot(title='Purchase Quantity Over Time')
plt.ylabel('Quantity Purchased')
plt.xlabel('Date')
plt.tight_layout()
plt.show()
