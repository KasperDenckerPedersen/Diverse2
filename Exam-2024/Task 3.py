import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales.csv')

#Total Sales per Store for the Year 2014: 
print("#Total Sales per Store for the Year 2014: ")

selector1 = sales['Date'] <= '2014-12-31'
selector2 = sales['Date'] >= '2014-01-01'
filteredSales = sales[selector1 & selector2]
total_sales_2024 = filteredSales.groupby('Store')['Sales'].sum()

print(total_sales_2024)

#Store with the Most Consistent Sales:	
print("#Store with the Most Consistent Sales:")

SalesStdDev = sales.groupby('Store')['Sales'].std().sort_values(ascending=True)
SalesStdDev = SalesStdDev.reset_index()
SalesStdDev.columns = ['Store', 'SalesStdDev']
SalesStdDev = SalesStdDev.set_index('Store')

print(SalesStdDev)

#Monthly Sales Trend for Each Store:
print("Monthly Sales Trend for Each Store:")

sales['Date'] = pd.to_datetime(sales['Date'])
sales['Month'] = sales['Date'].dt.to_period('M')
monthly_sales_trend = sales.groupby(['Store', 'Month'])['Sales'].sum().reset_index()
monthly_sales_trend.columns = ['Store', 'Month', 'TotalSales']
print(monthly_sales_trend)

#Sales Distribution by Day of the Week:
print("Sales Distribution by Day of the Week:")

def get_days(x):
    day = x['DayOfWeek']
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Thueday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"

sales["Day Of The Week"] = sales.apply(get_days, axis=1)

data = sales.groupby('Day Of The Week')['Sales'].mean().plot(kind="bar")
plt.show()

#Sales Trend for the Top 5 Stores:
total_sales = sales.groupby('Store')['Sales'].sum().sort_values(ascending=True)
print(total_sales.head(5))

Top5Stores = [307, 543, 198, 208, 263]

for store in Top5Stores:
    store_data = sales[sales['Store'] == store]
    plt.plot(store_data['Date'], store_data['Sales'], label=f'Store {store}')

plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend Over Time for Top 5 Stores')
plt.legend(title='Store')
plt.tight_layout() 
plt.show()