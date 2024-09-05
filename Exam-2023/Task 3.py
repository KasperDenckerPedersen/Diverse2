import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('Exam-2023/sales.csv')

#Query 1: What was each store’s average daily sales in June 2014.

june_2014_sales = sales[(sales['Date'] >= '2014-06-01') & (sales['Date'] <= '2014-06-30')]
data = june_2014_sales.groupby('Store')['Sales'].mean()
query1 = pd.DataFrame(data)
print("Query 1:")
print(query1)

#For each store identify the date with the highest sales in the whole period.
data = sales.loc[sales.groupby('Store')['Sales'].idxmax().sort_values(ascending=False)]
query2 = pd.DataFrame(data)
print("Query 2:")
print(query2)

#Identify the day of the week that has on average the highest sales across all stores
data = sales.groupby('DayOfWeek')['Sales'].mean()
query3 = pd.DataFrame(data)
print("Query 3:")
print(query3)

#Plot the evolution of the daily sales for the stores 1, 15, 27 and 90 over the entire data period.
stores = sales[sales['Store'].isin([1, 15, 27, 90])]
sales2 = stores.groupby(['Store', 'Date'])['Sales'].sum().reset_index()

for store in [1, 15, 27, 90]:
    plt.plot(sales2['Date'], sales2['Sales'], label=f'Store: {store}')
plt.title('Evolution of Daily Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(title='Store')
plt.show()

