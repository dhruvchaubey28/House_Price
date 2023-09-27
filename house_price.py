import requests
from bs4 import BeautifulSoup
class Property_list_fetcher:
  def fetch_property_listings(self, location):
        url = f"https://www.magicbricks.com/property-for-sale-rent-in-{location}-area"
        try:
            response = requests.get(url)
            response.raise_for_status()  # this will raise an exception if the request was unsuccessful
        except requests.exceptions.RequestException as E:
            print(f"Error: {str(E)}")
            return
  
