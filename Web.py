import sys
from PyQt5.QtCore import Qt
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

        self.name_label = QLabel("Credits: Dhruv & Ashlee", self)
        self.name_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)

        self.central_layout.addWidget(self.name_label)

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
