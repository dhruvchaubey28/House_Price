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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HousePriceChecker()
    main_window.show()
    sys.exit(app.exec_())
