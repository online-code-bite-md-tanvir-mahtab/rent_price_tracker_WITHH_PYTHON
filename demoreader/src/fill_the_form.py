from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
FORM_LINK_URI = "https://docs.google.com/forms/d/e/1FAIpQLSeK5s5tLlKmTsO_9-64UFia8voRgfZJ65oRfxpjXjFQuATWhQ/viewform?usp=sf_link"
EDGE_DRIVER_PATH = "G:\edgedriver_win64\msedgedriver.exe"

# creating the class
class FormFill:
    def __init__(self):
        self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)
    

    def find_the_form_fill(self,add,money,link):
        try:
            self.driver.get(url=FORM_LINK_URI)
            address = self.driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address.send_keys(add)
            taka = self.driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            taka.send_keys(money)
            li = self.driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            li.send_keys(link)
            sleep(4)
            submit = self.driver.find_element_by_xpath(xpath='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit.click()
            sleep(4)
        except NoSuchElementException:
            sleep(2)
            self.driver.quit()