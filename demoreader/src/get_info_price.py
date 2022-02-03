# from unicodedata import name
from unicodedata import name
from urllib import response
from bs4 import BeautifulSoup
import requests

# HOME_URI = "https://www.zillow.com/"
HOME_URI = 'https://www.zillow.com/homes/for_sale/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.68750190734863%2C%22east%22%3A-122.14779853820801%2C%22south%22%3A37.59754484771488%2C%22north%22%3A37.954986016611066%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'
LIST_OF_LINK = []
LIST_OF_PRICE = []
LIST_OF_ADDRESS = []
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
# creating the class
class HomePrice:
    def __init__(self):
        self.response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",headers=header)
        # geting the data
        self.data = self.response.text
        # geting the Beautifulsoup object
        self.soup = BeautifulSoup(self.data,'html.parser')
    

    def get_the_link_data(self)->list:
        all_link_list = self.soup.find_all("a",class_="list-card-link")
        for links in all_link_list:
            link = links['href']
            if 'https' in link:
                LIST_OF_LINK.append(link)
            else:
                LIST_OF_LINK.append(f"https://www.zillow.com/homedetails{link}/")
        return LIST_OF_LINK
    
    def get_the_price_data(self)->list:
        all_money_list = self.soup.find_all("div",class_="list-card-price")
        for price in all_money_list:
            money = price.getText()
            LIST_OF_PRICE.append(money)
        return LIST_OF_PRICE


    def get_the_address(self)->list:
        all_address_list = self.soup.find_all("address",class_='list-card-addr')
        for item in all_address_list:
            LIST_OF_ADDRESS.append(item.getText()) 
        return LIST_OF_ADDRESS