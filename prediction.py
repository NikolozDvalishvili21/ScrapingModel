import csv

def interpolate_sales(year1, sales1, year2, sales2, target_year):
    fraction = (target_year - year1) / (year2 - year1)
    predicted_sales = sales1 + (sales2 - sales1) * fraction
    return predicted_sales

sales_data = []
with open('elden_ring_sales.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        year = int(row['Year'])
        sales = int(row['Total Sales'])
        sales_data.append((year, sales))

sales_data.sort(key=lambda x: x[0])

sales_2022 = next(sales for year, sales in sales_data if year == 2022)
sales_2024 = next(sales for year, sales in sales_data if year == 2024)
actual_2023 = next(sales for year, sales in sales_data if year == 2023)

predicted_2023 = interpolate_sales(2022, sales_2022, 2024, sales_2024, 2023)

difference = predicted_2023 - actual_2023
percent_error = (difference / actual_2023) * 100

print("Data from CSV:")
for year, sales in sales_data:
    print(f"{year} Sales: {sales:,}")

print(f"\nAnalysis:")
print(f"Predicted 2023 Sales: {predicted_2023:,.2f}")
print(f"Actual 2023 Sales: {actual_2023:,}")
print(f"\nDifference: {difference:,.2f}")
print(f"Percentage Error: {percent_error:.2f}%")