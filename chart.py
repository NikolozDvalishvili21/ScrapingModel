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

sales_in_millions = [sales / 1_000_000 for sales in total_sales]

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(years, sales_in_millions, color=['blue', 'green', 'red'])  
plt.title('Total Sales for Elden Ring (2022 vs 2023 vs 2024) in Millions')
plt.xlabel('Year')
plt.ylabel('Total Sales (in millions)')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(sales_in_millions, labels=years, autopct='%1.1f%%', colors=['blue', 'green', 'red'])  
plt.title('Sales Distribution of Elden Ring (2022 vs 2023 vs 2024) in Percentage')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(years, sales_in_millions, s=100, color='red', marker='o')
plt.title('Scatter Plot of Sales Data (2022 vs 2023 vs 2024) in Millions')
plt.xlabel('Year')
plt.ylabel('Total Sales (in millions)')
plt.show()
