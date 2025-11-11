thonimport requests
from bs4 import BeautifulSoup

class PropertyParser:
    def __init__(self):
        self.base_url = "https://streeteasy.com"
    
    def parse_properties(self, url):
        properties = []
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        listings = soup.find_all("div", class_="property-card")
        for listing in listings:
            property_data = {
                "id": listing.get("data-id"),
                "price": listing.find("span", class_="price").text.strip(),
                "areaName": listing.find("span", class_="area-name").text.strip(),
                "bedroomCount": listing.find("span", class_="bedroom-count").text.strip(),
                "buildingType": listing.find("span", class_="building-type").text.strip(),
                "priceChangedAt": listing.find("time")["datetime"],
                "geoPoint": listing.get("data-geopoint"),
                "amenities": self.extract_amenities(listing),
                "photos": self.extract_photos(listing),
                "urlPath": self.base_url + listing.find("a")["href"]
            }
            properties.append(property_data)
        return properties
    
    def extract_amenities(self, listing):
        amenities = []
        amenities_list = listing.find_all("li", class_="amenity")
        for amenity in amenities_list:
            amenities.append(amenity.text.strip())
        return amenities
    
    def extract_photos(self, listing):
        photos = []
        images = listing.find_all("img", class_="property-image")
        for image in images:
            photos.append(image["src"])
        return photos