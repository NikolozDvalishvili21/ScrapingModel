import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_mbappe_goals(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.121 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    stats_pullout = soup.find('div', class_='stats_pullout')
    if not stats_pullout:
        print("Could not find the stats_pullout div.")
        return None

    goal_data_div = stats_pullout.find('div', class_='p1')
    if goal_data_div:
        goal_elements = goal_data_div.find_all('div')
        
        la_liga_goals = None
        champions_league_goals = None
        
        for div in goal_elements:
            if "Gls" in div.text:
                goals = div.find_all('p')
                if len(goals) >= 2: 
                    la_liga_goals = goals[0].text.strip()
                    champions_league_goals = goals[1].text.strip()
                    
                    print("La Liga Goals:", la_liga_goals)
                    print("Champions League Goals:", champions_league_goals)

                    data = {
                        "La Liga Goals": [la_liga_goals],
                        "Champions League Goals": [champions_league_goals]
                    }
                    df = pd.DataFrame(data)

                    df.to_csv('mbappe_goals_2024_2025.csv', index=False)
                    print("Goal data saved to 'mbappe_goals_2024_2025.csv'")

                    return df
    else:
        print("Goal data section not found.")
        return None

url = "https://fbref.com/en/players/42fd9c7f/Kylian-Mbappe"

goals_data = scrape_mbappe_goals(url)
if goals_data is not None:
    print("Goal data successfully scraped.")
else:
    print("Failed to extract goal data.")
