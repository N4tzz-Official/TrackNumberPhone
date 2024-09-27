import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

init(autoreset=True)

banner = f"""
{Fore.RED}  _   _ _  _   _            _____                       _   _______             _              
{Fore.GREEN} | \ | | || | | |          / ____|                     | | |__   __|           | |             
{Fore.YELLOW} |  \| | || |_| |_ _______| (___   __ _ _   _  __ _  __| |    | |_ __ __ _  ___| | _____ _ __  
{Fore.CYAN} | . ` |__   _| __|_  /_  /\___ \ / _` | | | |/ _` |/ _` |    | | '__/ _` |/ __| |/ / _ \ '__| 
{Fore.MAGENTA} | |\  |  | | | |_ / / / / ____) | (_| | |_| | (_| | (_| |    | | | | (_| | (__|   <  __/ |    
{Fore.BLUE} |_| \_|  |_|  \__/___/___|_____/ \__, |\__,_|\__,_|\__,_|    |_|_|  \__,_|\___|_|\_\___|_|    
{Fore.RED}                                     | |                                                     
{Fore.GREEN}                                     |_|                                                     
"""

def search_phone_number(phone_number):
    query = f"{phone_number} location"
    url = f"https://www.google.com/search?q={query}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    region = "N/A"
    province = "N/A"
    kabupaten = "N/A"
    kecamatan = "N/A"
    kelurahan = "N/A"
    desa = "N/A"
    street = "N/A"
    house_number = "N/A"
    carrier = "N/A"
    line_type = "N/A"

    for result in soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
        text = result.get_text()
        
        if "Indonesia" in text or "region" in text:
            region = text
        elif "Jawa" in text or "Sumatra" in text or "Bali" in text:
            province = text
        elif "Kabupaten" in text or "Kota" in text:
            kabupaten = text
        elif "Kecamatan" in text:
            kecamatan = text
        elif "Kelurahan" in text or "Desa" in text:
            kelurahan = text
        elif "Street" in text or "Jalan" in text:
            street = text
        elif "House No" in text or "No Rumah" in text:
            house_number = text
        if "Carrier" in text or "Telkomsel" in text or "Indosat" in text or "XL" in text:
            carrier = text
        elif "mobile" in text or "landline" in text:
            line_type = text

    print(f"Phone Number: {phone_number}")
    print(f"Region: {region}")
    print(f"Province: {province}")
    print(f"Kabupaten: {kabupaten}")
    print(f"Kecamatan: {kecamatan}")
    print(f"Kelurahan: {kelurahan}")
    print(f"Desa: {desa}")
    print(f"Street: {street}")
    print(f"House Number: {house_number}")
    print(f"Carrier: {carrier}")
    print(f"Line Type: {line_type}")

if __name__ == "__main__":
    print(banner)
    phone_number = input(Fore.YELLOW + "Number Phone: ")
    print(f"Searching public information for {phone_number}...\n")
    search_phone_number(phone_number)
