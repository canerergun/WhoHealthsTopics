import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.who.int/health-topics")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    basliklar = soup.find_all(class_="heading text-underline")
 
    for i in basliklar:
        print(i.get_text())
        print("-"*50)
