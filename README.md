### Phone Number Tracker
This Python script allows you to search for detailed public information about a phone number. It simulates obtaining information such as the region, province, district, sub-district, village, street, and house number, along with the carrier and line type.

### Features
Search for a phone number’s public details
Display information in a detailed format such as:
Region (Country)
Province
District (Kabupaten)
Sub-district (Kecamatan)
Village (Kelurahan)
Street and House Number
Carrier and Line Type
Installation
Requirements
Ensure you have the following installed:

Python 3.x
requests module
beautifulsoup4 module
colorama module
You can install the required modules using:

bash
Salin kode
pip install requests beautifulsoup4 colorama
Cloning the Repository
Clone this repository to your local machine:

bash
Salin kode
git clone https://github.com/N4tzz-Official/TrackNumberPhone.git
Navigate into the directory:

bash
Salin kode
cd TrackNumberPhone
Usage
To use the script, run it using Python:

bash
Salin kode
python phone_tracker.py
When prompted, enter the phone number in an international format (example: +62 811234567890).

### Example Output
yaml
Salin kode
Phone Number: +62 811234567890
Region: Indonesia
Province: Jawa Barat
Kabupaten: Kabupaten Bandung
Kecamatan: Kecamatan Sukasari
Kelurahan: Kelurahan Cipedes
Desa: Desa Mekarjaya
Street: Jalan Raya Cibiru No. 45
House Number: 101
Carrier: Telkomsel
Line Type: mobile
Disclaimer 
The information retrieved is simulated and may not represent real data. For accurate results, consider using a paid API service for phone number lookups. 😃
