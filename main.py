import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.vgchartz.com/game/230180/elden-ring/sales'

response = requests.get(url) # გეთ რექვესთის გაგზავნა რომ ავიღოთ HTML კონტენტი ურლდან

soup = BeautifulSoup(response.content, 'html.parser') # პარსავს ჰტმლ კონტენტს

table = soup.find('table', {'style': 'width:100%;'})  

# ცვლადები სადაც შეინახება დატა
total_2024 = 0
total_2023 = 0
total_2022 = 0

# გაპარსულ კონტენტში ამოწმებს არის თუარა თეიბლი
if not table:
    print("Table not found.")
else:
    print("Table found, proceeding with parsing.")


# ფორ ლუპი იმისთვის რომ ყველა როუ ანუ tr ელემენტი იპოვოს თეიბლში
for row in table.find_all('tr'):
    # ყველა როუსთვის ეძებს td ელემენტებს ანუ ქოლუმნებს
    columns = row.find_all('td')
    
    # თუ როუში არის 3 ან 3 ზე მეტი ქოლუმნი მაშინ პროცესდება შემდეგი ლოგიკა 
    if len(columns) >= 3:  
        # ვეძებთ a თაგს რადგან საიტზე a თეგში წერია დატა
        sales_str = columns[0].find('a')
        if sales_str:
            # ვაშორებთ a თაგში არსებულ კონტენტს ვაითსფეისებს
            sales_text = sales_str.get_text(strip=True)
            print(f"Extracted sales text: '{sales_text}'")  
            # გამოგვაქ მესამე ქოლუმნიდან წლების დატა
            date_str = columns[2].get_text(strip=True)
            print(f"Date extracted: '{date_str}'")  

            try:
                # ვაქცევთ ინტ-ად და ვაშორებთ მძიმეებს
                sales = int(sales_text.replace(',', ''))
                print(f"Converted sales: {sales}")  

                # რადგან წლები იყო დაყოფილი საიტზე, ვაჯამებთ
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

# CSV-სთვის თემფლეითი
data = [
    ['Year', 'Total Sales'],
    ['2024', total_2024],
    ['2023', total_2023],
    ['2022', total_2022]
]

csv_filename = 'elden_ring_sales.csv'
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    # იქმნება CSV writer object
    writer = csv.writer(file)
    # CSV-ში იწერება ზემოთ დაწერილი CSV თემფლეითი
    writer.writerows(data)

print(f"Data has been saved to {csv_filename}")
