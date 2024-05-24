import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.who.int/health-topics")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    basliklar = soup.find_all(class_="heading text-underline")
    kategoriler = soup.find_all(class_="date")


    for kategori, baslik in zip(kategoriler, basliklar):
        print(f"Kategori: {kategori.get_text().strip()}")
        print(f"Başlık: {baslik.get_text().strip()}")
        print("-" * 50)
else:
    print(f"Web sayfası alınamadı. Durum kodu: {response.status_code}")
