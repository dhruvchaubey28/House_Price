#importing important libraries
import requests  # Library for making HTTP requests
from bs4 import BeautifulSoup  #for parsing HTML

#creating a class
class PropertyListingsFetcher:
    #define a method for a given location
   def fetch_property_listings(self, location):
        # Create a URL
        url = f"https://www.magicbricks.com/property-for-sale-rent-in-{location}-area"
        try:
            response = requests.get(url)
            response.raise_for_status() # this will raise an exception if the request was unsuccessful
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}") #handle any request related errors
            return

        if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, 'html.parser')
                property_listings = soup.find_all("div", class_="m-srp-card") #find all properties on the page

                if property_listings:
                    listings_text = []
                    for idx, listing in enumerate(property_listings, start=1):
                        property_title = listing.find("span", class_="m-srp-card__title").text.strip()
                        listings_text.append(f"{idx}. {property_title}")
                    print("\n".join(listings_text))
                else:
                    print(f"No property listings found for {location}")
            except Exception as e:
                print(f"Error parsing data: {str(e)}")  #handle any parsing errors
        else:
           #will print error message if the https request fails
    	    print(f"Failed to retrieve data from Magicbricks.com for {location}")

def main():
    fetcher = Property_list_fetcher()  # Create an instance 
    location = input("Enter the location: ")  # Prompt the user to enter a location
    if location:
        # If a location is provided, fetch property listings for that location
        fetcher.fetch_property_listings(location)
    else:
        # If no location is provided, print a message asking for a location
        print("Please enter a location.")

#will if the script is being run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
