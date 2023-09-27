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
  if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, 'html.parser')
                property_listings = soup.find_all("div", class_="m-srp-card")

                if property_listings:
                    listings_text = []
                    for idx, listing in enumerate(property_listings, start=1):
                        property_title = listing.find("span", class_="m-srp-card__title").text.strip()
                        listings_text.append(f"{idx}. {property_title}")
                    print("\n".join(listings_text))
                else:
                    print(f"No property listings found for {location}")
                  except Exception as e:
                print(f"Error parsing data: {str(e)}")
        else:
            print(f"Failed to retrieve data from Magicbricks.com for {location}")
          def main():
    fetcher = Property_list_fetcher()
    location = input("Enter the location: ")
    if location:
        fetcher.fetch_property_listings(location)
    else:
        print("Please enter a location.")



            
