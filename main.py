import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.vgchartz.com/game/230180/elden-ring/sales'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'style': 'width:100%;'})  

total_2024 = 0
total_2023 = 0
total_2022 = 0

if not table:
    print("Table not found.")
else:
    print("Table found, proceeding with parsing.")

for row in table.find_all('tr'):
    columns = row.find_all('td')
    
    if len(columns) >= 3:  
        sales_str = columns[0].find('a')
        if sales_str:
            sales_text = sales_str.get_text(strip=True)
            print(f"Extracted sales text: '{sales_text}'")  

            date_str = columns[2].get_text(strip=True)
            print(f"Date extracted: '{date_str}'")  

            try:
                sales = int(sales_text.replace(',', ''))
                print(f"Converted sales: {sales}")  

                if '2024' in date_str:
                    total_2024 += sales
                    print(f"Added {sales} to total_2024. New total: {total_2024}")  
                elif '2023' in date_str:
                    total_2023 += sales
                    print(f"Added {sales} to total_2023. New total: {total_2023}")  
                elif '2022' in date_str:
                    total_2022 += sales
                    print(f"Added {sales} to total_2022. New total: {total_2022}")  
            except ValueError:
                print(f"Skipping invalid sales value: {sales_text}")  

print(f"Total sales in 2024: {total_2024}")
print(f"Total sales in 2023: {total_2023}")
print(f"Total sales in 2022: {total_2022}")

data = [
    ['Year', 'Total Sales'],
    ['2024', total_2024],
    ['2023', total_2023],
    ['2022', total_2022]
]

csv_filename = 'elden_ring_sales.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data has been saved to {csv_filename}")
