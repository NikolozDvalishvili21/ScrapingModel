# charts.py
import csv
import matplotlib.pyplot as plt

def read_sales_data(csv_filename):
    years = []
    sales = []
    
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            years.append(row[0])
            sales.append(int(row[1]))  
    
    return years, sales

csv_filename = 'elden_ring_sales.csv'

years, total_sales = read_sales_data(csv_filename)

plt.figure(figsize=(10, 6))
plt.bar(years, total_sales, color=['blue', 'green'])
plt.title('Total Sales for Elden Ring (2023 vs 2024)')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(total_sales, labels=years, autopct='%1.1f%%', colors=['blue', 'green'])
plt.title('Sales Distribution of Elden Ring (2023 vs 2024)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(years, total_sales, s=100, color='red', marker='o')
plt.title('Scatter Plot of Sales Data (2023 vs 2024)')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.show()
