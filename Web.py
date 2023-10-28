import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTextBrowser, QComboBox, QListWidget, QListWidgetItem
)

# Mock state data with district-wise house prices
state_data = {
    "Goa": {
        "Panaji": {
            "2 BHK Apartment for Sale in Miramar": "1.28 Cr",
            "3 BHK Villa for Sale in Dona Paula": "1.75 Cr",
            "4 BHK Apartment for Sale in Caranzalem": "2.10 Cr",
            "2 BHK Flat for Sale in St. Inez": "1.20 Cr",
            "3 BHK Penthouse for Sale in Taleigao": "2.35 Cr",
            "4 BHK Villa for Sale in Santa Cruz": "3.30 Cr",
        },
        "Vasco da Gama": {
            "2 BHK Apartment for Sale in Vasco (Central Location)": "1.30 Cr",
            "3 BHK Villa for Sale in Chicalim": "1.95 Cr",
            "3 BHK Apartment for Sale in Bogmalo Beach": "1.85 Cr",
            "2 BHK Flat for Sale in Cortalim": "1.18 Cr",
            "3 BHK Penthouse for Sale in Dabolim Airport Area": "2.50 Cr",
            "4 BHK Villa for Sale in Marmugao": "3.70 Cr",
            "3 BHK Villa for Sale in Dabolim": "1.65 Cr",
            "2 BHK Flat for Sale in Baina": "1.15 Cr",
        },
        "Ponda": {
            "2 BHK Apartment for Sale in Farmagudi": "1.08 Cr",
            "3 BHK Villa for Sale in Dhavali": "1.62 Cr",
            "4 BHK Apartment for Sale in Tisk": "1.72 Cr",
            "2 BHK Flat for Sale in Kundaim": "1.15 Cr",
            "3 BHK Penthouse for Sale in Marcela": "2.05 Cr",
            "4 BHK Villa for Sale in Mardol": "2.90 Cr",
            "3 BHK Apartment for Sale in Tisk": "1.30 Cr",
            "Plot/Land for sale in Ponda": "2.2 Cr",
            "5 BHK House for Sale in Raj Heritage,Ponda": "1.30 Cr",
        },
    },
    "Gujarat": {
        "Ahmedabad": {
            "2 BHK Apartment for Sale in Satellite": "1.15 Cr",
            "3 BHK Villa for Sale in Bodakdev": "1.80 Cr",
            "4 BHK Apartment for Sale in Prahladnagar": "1.50 Cr",
            "2 BHK Flat for Sale in Vastrapur": "1.05 Cr",
            "3 BHK Penthouse for Sale in Gota": "2.15 Cr",
            "4 BHK Villa for Sale in Thaltej": "2.75 Cr",
            "3 BHK Villa for Sale in Ahmedabad": "1.20 Cr",
            "2 BHK Flat for Sale in Ahmedabad": "85 Lakh",
        },
        "Surat": {
            "2 BHK Apartment for Sale in Surat": "80 Lakh",
            "3 BHK Villa for Sale in Surat": "1.10 Cr",
            "2 BHK Apartment for Sale in Adajan": "95 Lakh",
            "3 BHK Villa for Sale in Vesu": "1.40 Cr",
            "4 BHK Apartment for Sale in Piplod": "1.20 Cr",
            "2 BHK Flat for Sale in Varachha": "88 Lakh",
            "3 BHK Penthouse for Sale in Parle Point": "1.55 Cr",
            "4 BHK Villa for Sale in Dumas": "2.25 Cr",
        },
        "Vadodara": {
            "2 BHK Apartment for Sale in Vadodara": "75 Lakh",
            "2 BHK Apartment for Sale in Alkapuri": "1.08 Cr",
            "3 BHK Villa for Sale in Fatehgunj": "1.55 Cr",
            "4 BHK Apartment for Sale in Karelibaug": "1.35 Cr",
            "2 BHK Flat for Sale in Akota": "98 Lakh",
            "3 BHK Penthouse for Sale in Vasna Road": "1.65 Cr",
            "4 BHK Villa for Sale in Ajwa Road": "2.55 Cr",
            "3 BHK Villa for Sale in Vadodara": "95 Lakh",
        },
    },
    "Haryana": {
        "Chandigarh": {
            "2 BHK Apartment for Sale in Chandigarh": "1.05 Cr",
            "2 BHK Apartment for Sale in Zirakpur": "1.15 Cr",
            "3 BHK Villa for Sale in Mohali": "1.60 Cr",
            "4 BHK Apartment for Sale in Panchkula": "1.85 Cr",
            "2 BHK Flat for Sale in Sector 35": "1.10 Cr",
            "3 BHK Penthouse for Sale in Sector 22": "2.25 Cr",
            "4 BHK Villa for Sale in Kharar": "2.95 Cr",
            "3 BHK Villa for Sale in Chandigarh": "1.40 Cr",
        },
        "Faridabad": {
            "2 BHK Apartment for Sale in Faridabad": "80 Lakh",
            "2 BHK Apartment for Sale in Sector 14": "85 Lakh",
            "3 BHK Villa for Sale in Sector 21": "1.25 Cr",
            "4 BHK Apartment for Sale in Sector 37": "1.40 Cr",
            "2 BHK Flat for Sale in Sector 48": "90 Lakh",
            "3 BHK Penthouse for Sale in Sector 30": "1.75 Cr",
            "4 BHK Villa for Sale in Sector 16": "2.10 Cr",
            "3 BHK Villa for Sale in Faridabad": "1.10 Cr",
        },
        "Gurgaon": {
            "2 BHK Apartment for Sale in Gurgaon": "1.20 Cr",
            "2 BHK Apartment for Sale in DLF Phase 4": "1.30 Cr",
            "3 BHK Villa for Sale in Sohna Road": "1.90 Cr",
            "4 BHK Apartment for Sale in Golf Course Extension": "2.25 Cr",
            "2 BHK Flat for Sale in MG Road": "1.45 Cr",
            "3 BHK Penthouse for Sale in Sector 56": "2.75 Cr",
            "4 BHK Villa for Sale in Palam Vihar": "3.40 Cr",
            "3 BHK Villa for Sale in Gurgaon": "1.65 Cr",
        },
        "Panipat": {
            "2 BHK Apartment for Sale in Panipat": "70 Lakh",
            "2 BHK Apartment for Sale in Model Town": "75 Lakh",
            "3 BHK Villa for Sale in Huda Sector 11": "1.05 Cr",
            "4 BHK Apartment for Sale in Sanjay Colony": "1.20 Cr",
            "2 BHK Flat for Sale in Tehsil Camp": "80 Lakh",
            "3 BHK Penthouse for Sale in Nalwa Colony": "1.40 Cr",
            "4 BHK Villa for Sale in Assandh Road": "1.80 Cr",
            "3 BHK Villa for Sale in Panipat": "90 Lakh",
        },
        "Ambala": {
            "2 BHK Apartment for Sale in Ambala": "60 Lakh",
            "2 BHK Apartment for Sale in Ambala Cantt": "68 Lakh",
            "3 BHK Villa for Sale in Baldev Nagar": "92 Lakh",
            "4 BHK Apartment for Sale in Sector 8": "1.10 Cr",
            "2 BHK Flat for Sale in Jagadhri Road": "75 Lakh",
            "3 BHK Penthouse for Sale in Mahesh Nagar": "1.25 Cr",
            "4 BHK Villa for Sale in Shahzadpur": "1.65 Cr",
            "3 BHK Villa for Sale in Ambala": "80 Lakh",
        },
    },
    "Madhya Pradesh": {
        "Bhopal": {
            "2 BHK Apartment for Sale in Bhopal": "60 Lakh",
            "2 BHK Apartment for Sale in Arera Colony": "65 Lakh",
            "3 BHK Villa for Sale in Shyamla Hills": "90 Lakh",
            "4 BHK Apartment for Sale in Kolar Road": "1.15 Cr",
            "2 BHK Flat for Sale in Misrod": "70 Lakh",
            "3 BHK Penthouse for Sale in Ayodhya Bypass": "1.30 Cr",
            "4 BHK Villa for Sale in Bagh Mungaliya": "1.75 Cr",
            "3 BHK Villa for Sale in Bhopal": "80 Lakh",
        },
        "Indore": {
            "2 BHK Apartment for Sale in Indore": "65 Lakh",
            "2 BHK Apartment for Sale in Vijay Nagar": "70 Lakh",
            "3 BHK Villa for Sale in Saket Nagar": "95 Lakh",
            "4 BHK Apartment for Sale in Bengali Square": "1.20 Cr",
            "2 BHK Flat for Sale in Palasia": "75 Lakh",
            "3 BHK Penthouse for Sale in Rajendra Nagar": "1.40 Cr",
            "4 BHK Villa for Sale in Khandwa Road": "1.90 Cr",
            "3 BHK Villa for Sale in Indore": "85 Lakh",
        },
        "Gwalior": {
            "2 BHK Apartment for Sale in Gwalior": "55 Lakh",
            "2 BHK Apartment for Sale in Lashkar": "52 Lakh",
            "3 BHK Villa for Sale in City Center": "72 Lakh",
            "4 BHK Apartment for Sale in Thatipur": "95 Lakh",
            "2 BHK Flat for Sale in Morar": "48 Lakh",
            "3 BHK Penthouse for Sale in Maharaj Bada": "1.10 Cr",
            "4 BHK Villa for Sale in Gole Ka Mandir": "1.35 Cr",
            "3 BHK Villa for Sale in Gwalior": "75 Lakh",
        },
        "Jabalpur": {
            "2 BHK Apartment for Sale in Jabalpur": "70 Lakh",
            "2 BHK Apartment for Sale in Civil Lines": "68 Lakh",
            "3 BHK Villa for Sale in Napier Town": "88 Lakh",
            "4 BHK Apartment for Sale in Wright Town": "1.15 Cr",
            "2 BHK Flat for Sale in Sadar Cantt": "62 Lakh",
            "3 BHK Penthouse for Sale in Gorakhpur": "1.25 Cr",
            "4 BHK Villa for Sale in Vijay Nagar": "1.60 Cr",
            "3 BHK Villa for Sale in Jabalpur": "90 Lakh",
        },
        "Ujjain": {
            "2 BHK Apartment for Sale in Ujjain": "50 Lakh",
            "2 BHK Apartment for Sale in Freeganj": "48 Lakh",
            "3 BHK Villa for Sale in Nanakheda": "62 Lakh",
            "4 BHK Apartment for Sale in Vikram Nagar": "78 Lakh",
            "2 BHK Flat for Sale in Dewas Road": "45 Lakh",
            "3 BHK Penthouse for Sale in Mahakal Road": "1.05 Cr",
            "4 BHK Villa for Sale in Ksheer Sagar": "1.25 Cr",
            "3 BHK Villa for Sale in Ujjain": "70 Lakh",
        },
    },
    "Maharashtra": {
        "Mumbai": {
            "2 BHK Apartment for Sale in Mumbai": "2 Cr",
            "2 BHK Apartment for Sale in Bandra": "2.25 Cr",
            "3 BHK Villa for Sale in Juhu": "4.50 Cr",
            "4 BHK Apartment for Sale in Worli Sea Face": "5.75 Cr",
            "2 BHK Flat for Sale in Andheri West": "1.90 Cr",
            "3 BHK Penthouse for Sale in Powai": "3.80 Cr",
            "4 BHK Villa for Sale in Malabar Hill": "7.25 Cr",
            "3 BHK Villa for Sale in Navi Mumbai": "3 Cr",
        },
        "Pune": {
            "2 BHK Apartment for Sale in Pune": "90 Lakh",
            "2 BHK Apartment for Sale in Hinjewadi": "1.10 Cr",
            "3 BHK Villa for Sale in Kothrud": "1.75 Cr",
            "4 BHK Apartment for Sale in Magarpatta City": "2.20 Cr",
            "2 BHK Flat for Sale in Wakad": "95 Lakh",
            "3 BHK Penthouse for Sale in Baner": "1.40 Cr",
            "4 BHK Villa for Sale in Hadapsar": "2.60 Cr",
            "3 BHK Villa for Sale in Pune": "1.20 Cr",
        },
        "Thane": {
            "2 BHK Apartment for Sale in Thane": "95 Lakh",
            "2 BHK Apartment for Sale in Ghodbunder Road": "1.05 Cr",
            "3 BHK Villa for Sale in Majiwada": "1.60 Cr",
            "4 BHK Apartment for Sale in Kasarvadavali": "2.10 Cr",
            "2 BHK Flat for Sale in Vartak Nagar": "90 Lakh",
            "3 BHK Penthouse for Sale in Manpada": "1.30 Cr",
            "4 BHK Villa for Sale in Hiranandani Estate": "2.40 Cr",
            "3 BHK Villa for Sale in puri": "1.30 Cr",
        },
    },
    "Punjab": {
        "Amritsar": {
            "2 BHK Apartment for Sale in Amritsar": "65 Lakh",
            "2 BHK Apartment for Sale in Green Avenue": "62 Lakh",
            "3 BHK Villa for Sale in Ranjit Avenue": "82 Lakh",
            "4 BHK Apartment for Sale in Majitha Road": "1.05 Cr",
            "2 BHK Flat for Sale in Putlighar": "58 Lakh",
            "3 BHK Penthouse for Sale in Golden Temple Road": "1.20 Cr",
            "4 BHK Villa for Sale in Tarn Taran Road": "1.45 Cr",
            "3 BHK Villa for Sale in Amritsar": "85 Lakh",
        },
        "Ludhiana": {
            "2 BHK Apartment for Sale in Ludhiana": "70 Lakh",
            "2 BHK Apartment for Sale in Model Town": "68 Lakh",
            "3 BHK Villa for Sale in Sarabha Nagar": "88 Lakh",
            "4 BHK Apartment for Sale in Dugri": "1.15 Cr",
            "2 BHK Flat for Sale in Shaheed Bhagat Singh Nagar": "62 Lakh",
            "3 BHK Penthouse for Sale in Rajguru Nagar": "1.25 Cr",
            "4 BHK Villa for Sale in Gill Road": "1.60 Cr",
            "3 BHK Villa for Sale in Ludhiana": "90 Lakh",
        },
        "Jalandhar": {
            "2 BHK Apartment for Sale in Jalandhar": "60 Lakh",
            "2 BHK Apartment for Sale in Model Town": "58 Lakh",
            "3 BHK Villa for Sale in Lajpat Nagar": "78 Lakh",
            "4 BHK Apartment for Sale in Adampur": "95 Lakh",
            "2 BHK Flat for Sale in Urban Estate": "55 Lakh",
            "3 BHK Penthouse for Sale in Nakodar Road": "1.10 Cr",
            "4 BHK Villa for Sale in Basti Bawa Khel": "1.35 Cr",
            "3 BHK Villa for Sale in Jalandhar": "80 Lakh",
        },
        "Patiala": {
            "2 BHK Apartment for Sale in Patiala": "65 Lakh",
            "2 BHK Apartment for Sale in Urban Estate Phase 1": "62 Lakh",
            "3 BHK Villa for Sale in Model Town": "82 Lakh",
            "4 BHK Apartment for Sale in Tripuri": "1.05 Cr",
            "2 BHK Flat for Sale in Rajpura Road": "58 Lakh",
            "3 BHK Penthouse for Sale in Samana Road": "1.20 Cr",
            "4 BHK Villa for Sale in Bhadson Road": "1.45 Cr",
            "3 BHK Villa for Sale in Patiala": "85 Lakh",
        },
        "Bathinda": {
            "2 BHK Apartment for Sale in Bathinda": "55 Lakh",
            "2 BHK Apartment for Sale in Model Town": "52 Lakh",
            "3 BHK Villa for Sale in Goniana Road": "72 Lakh",
            "4 BHK Apartment for Sale in Mansa Road": "95 Lakh",
            "2 BHK Flat for Sale in Thermal Colony": "48 Lakh",
            "3 BHK Penthouse for Sale in Paras Ram Nagar": "1.10 Cr",
            "4 BHK Villa for Sale in Bhagta Bhai Ka": "1.35 Cr",
            "3 BHK Villa for Sale in Bathinda": "75 Lakh",
        },
    },
    "Rajasthan": {
        "Jaipur": {
            "2 BHK Apartment for Sale in Jaipur": "70 Lakh",
            "2 BHK Apartment for Sale in Vaishali Nagar": "75 Lakh",
            "3 BHK Villa for Sale in Malviya Nagar": "1.10 Cr",
            "4 BHK Apartment for Sale in Mansarovar": "1.40 Cr",
            "2 BHK Flat for Sale in Jagatpura": "68 Lakh",
            "3 BHK Penthouse for Sale in Shyam Nagar": "1.25 Cr",
            "4 BHK Villa for Sale in Civil Lines": "2.20 Cr",
            "3 BHK Villa for Sale in Jaipur": "90 Lakh",
        },
        "Jodhpur": {
            "2 BHK Apartment for Sale in Jodhpur": "75 Lakh",
            "2 BHK Apartment for Sale in Ratanada": "68 Lakh",
            "3 BHK Villa for Sale in Sardarpura": "88 Lakh",
            "4 BHK Apartment for Sale in Shastri Nagar": "1.15 Cr",
            "2 BHK Flat for Sale in Chopasni Housing Board": "62 Lakh",
            "3 BHK Penthouse for Sale in Pal Road": "1.40 Cr",
            "4 BHK Villa for Sale in Suncity": "2.60 Cr",
            "3 BHK Villa for Sale in Jodhpur": "95 Lakh",
        },
        "Udaipur": {
            "2 BHK Apartment for Sale in Udaipur": "65 Lakh",
            "2 BHK Apartment for Sale in Hiran Magri": "60 Lakh",
            "3 BHK Villa for Sale in Shobhagpura": "80 Lakh",
            "4 BHK Apartment for Sale in Fatehpura": "1.05 Cr",
            "2 BHK Flat for Sale in Ambamata": "55 Lakh",
            "3 BHK Penthouse for Sale in Pratap Nagar": "1.20 Cr",
            "4 BHK Villa for Sale in Bhuwana": "1.45 Cr",
            "3 BHK Villa for Sale in Udaipur": "85 Lakh",
        },
        "Kota": {
            "2 BHK Apartment for Sale in Kota": "80 Lakh",
            "2 BHK Apartment for Sale in Talwandi": "72 Lakh",
            "3 BHK Villa for Sale in Vigyan Nagar": "92 Lakh",
            "4 BHK Apartment for Sale in Kunhari": "1.20 Cr",
            "2 BHK Flat for Sale in Dadabari": "68 Lakh",
            "3 BHK Penthouse for Sale in Mahaveer Nagar": "1.35 Cr",
            "4 BHK Villa for Sale in Rajeev Gandhi Nagar": "1.70 Cr",
            "3 BHK Villa for Sale in Kota": "1 Cr",
        },
        "Ajmer": {
            "2 BHK Apartment for Sale in Ajmer": "60 Lakh",
            "2 BHK Apartment for Sale in Vaishali Nagar": "58 Lakh",
            "3 BHK Villa for Sale in Civil Lines": "78 Lakh",
            "4 BHK Apartment for Sale in Kishangarh Road": "95 Lakh",
            "2 BHK Flat for Sale in Nasirabad Road": "52 Lakh",
            "3 BHK Penthouse for Sale in Beawar": "1.10 Cr",
            "4 BHK Villa for Sale in Pushkar Road": "1.35 Cr",
            "3 BHK Villa for Sale in Ajmer": "80 Lakh",

        },
    },
    "Tamil Nadu": {
        "Chennai": {
            "2 BHK Apartment for Sale in Chennai": "1.10 Cr",
            "2 BHK Apartment for Sale in Adyar": "1.25 Cr",
            "3 BHK Villa for Sale in Velachery": "1.60 Cr",
            "4 BHK Apartment for Sale in Mylapore": "2.10 Cr",
            "2 BHK Flat for Sale in T. Nagar": "1.10 Cr",
            "3 BHK Penthouse for Sale in Anna Nagar": "1.75 Cr",
            "4 BHK Villa for Sale in Ekkatuthangal": "2.50 Cr",
            "3 BHK Villa for Sale in Chennai": "1.45 Cr",
        },
        "Madurai": {
            "2 BHK Apartment for Sale in Madurai": "80 Lakh",
            "2 BHK Apartment for Sale in Anna Nagar": "85 Lakh",
            "3 BHK Villa for Sale in KK Nagar": "1.20 Cr",
            "4 BHK Apartment for Sale in Kamarajar Salai": "1.75 Cr",
            "2 BHK Flat for Sale in Thiruparankundram": "78 Lakh",
            "3 BHK Penthouse for Sale in Alagar Kovil Road": "1.35 Cr",
            "4 BHK Villa for Sale in Vilachery": "2 Cr",
            "3 BHK Villa for Sale in Madurai": "1.05 Cr",
        },
        "Salem": {
            "2 BHK Apartment for Sale in Salem": "70 Lakh",
            "2 BHK Apartment for Sale in Hasthampatti": "72 Lakh",
            "3 BHK Villa for Sale in Alagapuram": "95 Lakh",
            "4 BHK Apartment for Sale in Shevapet": "1.30 Cr",
            "2 BHK Flat for Sale in Fair Lands": "68 Lakh",
            "3 BHK Penthouse for Sale in Gugai": "1.15 Cr",
            "4 BHK Villa for Sale in Kondalampatti": "1.60 Cr",
            "3 BHK Villa for Sale in Salem": "90 Lakh",
        },
    },
    "Uttar Pradesh": {
        "Lucknow": {
            "2 BHK Apartment for Sale in Lucknow": "75 Lakh",
            "2 BHK Apartment for Sale in Gomti Nagar": "85 Lakh",
            "3 BHK Villa for Sale in Alambagh": "1.10 Cr",
            "4 BHK Apartment for Sale in Indira Nagar": "1.40 Cr",
            "2 BHK Flat for Sale in Hazratganj": "78 Lakh",
            "3 BHK Penthouse for Sale in Mahanagar": "1.25 Cr",
            "4 BHK Villa for Sale in Jankipuram": "2 Cr",
            "3 BHK Villa for Sale in Lucknow": "95 Lakh",
        },
        "Kanpur": {
            "2 BHK Apartment for Sale in Kanpur": "60 Lakh",
            "2 BHK Apartment for Sale in Civil Lines": "72 Lakh",
            "3 BHK Villa for Sale in Kakadeo": "88 Lakh",
            "4 BHK Apartment for Sale in Swaroop Nagar": "1.15 Cr",
            "2 BHK Flat for Sale in Kidwai Nagar": "68 Lakh",
            "3 BHK Penthouse for Sale in Mall Road": "1.40 Cr",
            "4 BHK Villa for Sale in Naubasta": "2.60 Cr",
            "3 BHK Villa for Sale on Raja Road": "80 Lakh",
        },
        "Varanasi": {
            "2 BHK Apartment for Sale in Varanasi": "70 Lakh",
            "2 BHK Apartment for Sale in Sigra": "60 Lakh",
            "3 BHK Villa for Sale in Lanka": "78 Lakh",
            "4 BHK Apartment for Sale in Mahmoorganj": "95 Lakh",
            "2 BHK Flat for Sale in Paharia": "52 Lakh",
            "3 BHK Penthouse for Sale in Shivpur": "1.10 Cr",
            "4 BHK Villa for Sale in Sarnath": "1.35 Cr",
            "3 BHK Villa for Sale in Varanasi": "90 Lakh",
        },
        "Agra": {
            "2 BHK Apartment for Sale in Agra": "65 Lakh",
            "2 BHK Apartment for Sale in Sikandra": "58 Lakh",
            "3 BHK Villa for Sale in Tajganj": "78 Lakh",
            "4 BHK Apartment for Sale in Dayal Bagh": "95 Lakh",
            "2 BHK Flat for Sale in Sanjay Place": "52 Lakh",
            "3 BHK Penthouse for Sale in Fatehabad Road": "1.10 Cr",
            "4 BHK Villa for Sale in Bodla": "1.35 Cr",
            "3 BHK Villa for Sale in Vaibhav Nagar": "85 Lakh",
        },
    },
    "Uttarakhand": {
        "Dehradun": {
            "2 BHK Apartment for Sale in Dehradun": "80 Lakh",
            "2 BHK Apartment for Sale in Rajpur Road": "85 Lakh",
            "3 BHK Villa for Sale in Sahastradhara": "1.15 Cr",
            "4 BHK Apartment for Sale in Ballupur": "1.70 Cr",
            "2 BHK Flat for Sale in Clement Town": "80 Lakh",
            "3 BHK Penthouse for Sale in Dalanwala": "1.35 Cr",
            "4 BHK Villa for Sale in Doiwala": "2.00 Cr",
            "3 BHK Villa for Sale in Dehradun": "1.10 Cr",
        },
        "Haridwar": {
            "2 BHK Apartment for Sale in Haridwar": "70 Lakh",
            "1 BHK Apartment for Sale in Bhadrabad": "38 Lakh",
            "4 BHK Villa for Sale in Jagjeetpur": "2 Cr",
            "3 BHK Apartment for Sale in Shantikunj": "1.30 Cr",
            "2 BHK Flat for Sale in Kankhal": "48 Lakh",
            "4 BHK Penthouse for Sale in Patanjali Yogpeeth": "2.40 Cr",
            "3 BHK Villa for Sale in BHEL Township": "1.75 Cr",
            "3 BHK Villa for Sale in Haridwar": "90 Lakh",
        },
        "Rishikesh": {
            "2 BHK Apartment for Sale in Rishikesh": "75 Lakh",
            "1 BHK Apartment for Sale in Laxman Jhula": "40 Lakh",
            "4 BHK Villa for Sale in Tapovan": "2.10 Cr",
            "3 BHK Apartment for Sale in Muni Ki Reti": "1.15 Cr",
            "2 BHK Flat for Sale in Swarg Ashram": "52 Lakh",
            "4 BHK Penthouse for Sale in Neelkanth Road": "2.30 Cr",
            "3 BHK Villa for Sale in Shyampur": "1.90 Cr",
            "3 BHK Villa for Sale in Rishikesh": "95 Lakh",
        },
    },
    "West Bengal": {
        "Kolkata": {
            "2 BHK Apartment for Sale in Kolkata": "1.20 Cr",
            "1 BHK Apartment for Sale in Salt Lake City": "90 Lakh",
            "4 BHK Villa for Sale in Behala": "2.40 Cr",
            "3 BHK Apartment for Sale in Park Street": "1.60 Cr",
            "2 BHK Flat for Sale in Jadavpur": "70 Lakh",
            "4 BHK Penthouse for Sale in New Alipore": "2.80 Cr",
            "3 BHK Villa for Sale in Rajarhat": "1.90 Cr",
            "3 BHK Villa for Sale in Kolkata": "1.50 Cr",
        },
        "Durgapur": {
            "2 BHK Apartment for Sale in Durgapur": "70 Lakh",
            "1 BHK Apartment for Sale in Bidhannagar": "35 Lakh",
            "4 BHK Villa for Sale in City Center": "1.80 Cr",
            "3 BHK Apartment for Sale in Benachity": "1.10 Cr",
            "2 BHK Flat for Sale in Fuljhore": "45 Lakh",
            "4 BHK Penthouse for Sale in Steel Township": "2.20 Cr",
            "3 BHK Villa for Sale in Muchipara": "1.50 Cr",
            "3 BHK Villa for Sale in Durgapur": "90 Lakh",
        },
        "Howrah": {
            "2 BHK Apartment for Sale in Howrah": "85 Lakh",
            "1 BHK Apartment for Sale in Shibpur": "40 Lakh",
            "4 BHK Villa for Sale in Santragachi": "2.10 Cr",
            "3 BHK Apartment for Sale in Ballygunge": "1.25 Cr",
            "2 BHK Flat for Sale in Salkia": "50 Lakh",
            "4 BHK Penthouse for Sale in Liluah": "2.40 Cr",
            "3 BHK Villa for Sale in Uluberia": "1.70 Cr",
            "3 BHK Villa for Sale in Howrah": "1.10 Cr",

        },
    },
}

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QTextBrowser, QPushButton, QListWidget, QListWidgetItem

# Assuming you have a dictionary called 'state_data' with house price information

class HousePriceChecker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("House Price Checker")
        self.setGeometry(550, 220, 900, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.history_label = QLabel("Records", self)  # Added QLabel for the history label

        self.history_list = QListWidget(self)
        self.history_list.setFixedWidth(400)

        self.history_layout = QVBoxLayout()
        self.history_layout.addWidget(self.history_label)
        self.history_layout.addWidget(self.history_list)

        self.history_widget = QWidget()
        self.history_widget.setLayout(self.history_layout)

        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.addWidget(self.history_widget)

        self.state_prices_view = self.create_state_prices_view()
        self.central_layout.addWidget(self.state_prices_view)

        self.state_prices_view2 = self.create_state_prices_view2()
        self.central_layout.addWidget(self.state_prices_view2)

    def create_state_prices_view(self):
        state_prices_widget = QWidget(self)

        layout = QVBoxLayout()

        state_prices_label = QLabel("State-wise House Prices in India")
        layout.addWidget(state_prices_label)

        self.city_combobox = QComboBox(self)
        self.city_combobox.addItem("Select State")
        self.city_combobox.addItems(state_data.keys())
        layout.addWidget(self.city_combobox)

        self.district_combobox = QComboBox(self)
        self.district_combobox.addItem("Select City")
        layout.addWidget(self.district_combobox)

        self.state_prices_text = QTextBrowser(self)
        layout.addWidget(self.state_prices_text)

        show_prices_button = QPushButton("Show Prices", self)
        show_prices_button.clicked.connect(self.show_prices)
        layout.addWidget(show_prices_button)

        state_prices_widget.setLayout(layout)

        # Connect the city_combobox to update district_combobox
        self.city_combobox.currentIndexChanged.connect(self.update_district_combobox)

        return state_prices_widget

    def create_state_prices_view2(self):
        state_prices_widget = QWidget(self)

        layout = QVBoxLayout()

        state_prices_label = QLabel("State-wise House Prices in India (City 2)")
        layout.addWidget(state_prices_label)

        self.city_combobox2 = QComboBox(self)
        self.city_combobox2.addItem("Select State")
        self.city_combobox2.addItems(state_data.keys())
        layout.addWidget(self.city_combobox2)

        self.district_combobox2 = QComboBox(self)
        self.district_combobox2.addItem("Select City")
        layout.addWidget(self.district_combobox2)

        self.state_prices_text2 = QTextBrowser(self)
        layout.addWidget(self.state_prices_text2)

        compare_prices_button = QPushButton("Compare Prices", self)
        compare_prices_button.clicked.connect(self.compare_prices)
        layout.addWidget(compare_prices_button)

        state_prices_widget.setLayout(layout)

        # Connect the city_combobox2 to update district_combobox2
        self.city_combobox2.currentIndexChanged.connect(self.update_district_combobox2)

        return state_prices_widget

    def update_district_combobox(self):
        selected_city = self.city_combobox.currentText()
        self.district_combobox.clear()
        self.district_combobox.addItem("Select City")

        if selected_city != "Select State":
            self.district_combobox.addItems(state_data.get(selected_city, {}).keys())

    def update_district_combobox2(self):
        selected_city = self.city_combobox2.currentText()
        self.district_combobox2.clear()
        self.district_combobox2.addItem("Select City")

        if selected_city != "Select State":
            self.district_combobox2.addItems(state_data.get(selected_city, {}).keys())

    def show_prices(self):
        selected_city = self.city_combobox.currentText()
        selected_district = self.district_combobox.currentText()

        if selected_city == "Select State" or selected_district == "Select City":
            self.state_prices_text.setPlainText("Please select a city and district to view house prices.")
        else:
            district_prices = state_data.get(selected_city, {}).get(selected_district, "Not Available")
            formatted_prices = "\n".join(
                [f"- {property_name}: {price}" for property_name, price in district_prices.items()])

            message = f"House Prices in {selected_district}, {selected_city}:\n{formatted_prices}"
            self.state_prices_text.setPlainText(message)

        # Add user record to history list
        user_record = f" -> {selected_city}, {selected_district}"
        item = QListWidgetItem(user_record)
        self.history_list.addItem(item)

    def compare_prices(self):
        selected_city1 = self.city_combobox.currentText()
        selected_district1 = self.district_combobox.currentText()
        selected_city2 = self.city_combobox2.currentText()
        selected_district2 = self.district_combobox2.currentText()

        if (
            selected_city1 == "Select State" or selected_district1 == "Select City" or
            selected_city2 == "Select State" or selected_district2 == "Select City"
        ):
            self.state_prices_text.setPlainText("Please select two cities and districts to compare house prices.")
            self.state_prices_text2.setPlainText("")
        else:
            district_prices1 = state_data.get(selected_city1, {}).get(selected_district1, "Not Available")
            formatted_prices1 = "\n".join(
                [f"- {property_name}: {price}" for property_name, price in district_prices1.items()])

            district_prices2 = state_data.get(selected_city2, {}).get(selected_district2, "Not Available")
            formatted_prices2 = "\n".join(
                [f"- {property_name}: {price}" for property_name, price in district_prices2.items()])

            message1 = f"House Prices in {selected_district1}, {selected_city1}:\n{formatted_prices1}"
            message2 = f"House Prices in {selected_district2}, {selected_city2}:\n{formatted_prices2}"

            self.state_prices_text.setPlainText(message1)
            self.state_prices_text2.setPlainText(message2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HousePriceChecker()
    main_window.show()
    sys.exit(app.exec_())
