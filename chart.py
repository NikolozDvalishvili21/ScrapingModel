import csv
import matplotlib.pyplot as plt

def read_sales_data(csv_filename):
    # აქ სხვადასხვა ერეიებში ემატება წლები და გაყიდვები
    years = []
    sales = []
    
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ტოვებს ჰედერ როუს
        for row in reader:
            # append-ს ვუკეთებთ პირველ და მეორე როუს სადაც სეილები და წლები წერია
            years.append(row[0])
            sales.append(int(row[1]))  
    
    return years, sales

csv_filename = 'elden_ring_sales.csv'

# ვაბრუნებთ წლებს და ტოტალ სეილებს

years, total_sales = read_sales_data(csv_filename)

# უბრალოდ მარტივი გარჩევადობისთვის ვაკონვერტებ მილიონებს. (მაგალითად: 59 500 000 ხდება 59.5)
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
