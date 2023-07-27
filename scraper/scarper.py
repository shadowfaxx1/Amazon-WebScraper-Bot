import types
import typing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import os
from selenium.webdriver.common.keys import Keys as keys
import time 
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from prettytable import PrettyTable 
from scraper.constants import url 
from scraper.constants import link_list,price_list,initializer

import os
from selenium import webdriver
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
class amazon(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\kaifk\lpth\selenium", teardown=False, headless=True) -> None:
        self.driver_path = driver_path
        self.teardown = teardown
        self.headless = headless
        
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--user-data-dir=C:/Users/kaifk/AppData/Local/Google/Chrome/User Data/Profile 1")
        if self.headless:
            chrome_options.add_argument("--headless")

        # Use the 'options' argument instead of 'chrome_options'
        os.environ['PATH'] += os.pathsep + self.driver_path
        super(amazon, self).__init__(options=chrome_options)
        self.implicitly_wait(10)
        self.maximize_window()

    def search_items(self):
        j = 0
        all_items_info = []
        for i in link_list:
            item_info = self.search_url(i, price_list[j])
            all_items_info.append(item_info)
            j += 1
            self.refresh()
            if j == 1:
                break

        return all_items_info

    def search_url(self, item_link, expected_price):
        
        flag=self.perform_search(item_link)
        time.sleep(0.2)
        if(flag==0):
             return ["None","None","None","None",None]
            
        price = self.get_item_price()
        print(price)
        merchant_info = self.get_merchant_info()
        print(merchant_info)

        price_ET = None
        if merchant_info != "ETrade Online":
            price_ET = self.get_ETrade_price()
        
        price = price.replace(',', '')  # Remove the comma from the string
        price = int(price) 

        Et_live = "yes" if merchant_info == "ETrade Online" else "No"
        Et_mop = "yes" if (price) == (expected_price) else "No"
        bb_seller_p = None if price == expected_price else price
        bb_seller_name = merchant_info

        return [Et_live, Et_mop, bb_seller_p, bb_seller_name, price_ET]
    

    def perform_search(self, item_link):
        search_bar=self.get(f"https://www.amazon.in/d/{item_link}")
        time.sleep(0.5)
        if(self.is_present() ==0):
               return 0

    
    def get_item_price(self):
            
        
            try:
                price_element = WebDriverWait(self, 10).until(
                    ec.visibility_of_element_located((By.XPATH, '//span[@class="a-price-whole"]'))
                )
                price=price_element.text
            except Exception as NoSuchElementException:
                 price_element = WebDriverWait(self, 10).until(
                    ec.visibility_of_element_located((By.XPATH, '//span[@data-a-size="xl" and @data-a-color="base"]'))
                )
                 price=price_element.text
            
            except Exception as e:
                 price = "0"

            return price
    
    def is_present(self):
        try:
            outOfStock = self.find_element(By.ID, "outOfStock")
            return 0
        except NoSuchElementException:
            pass
        try:
            unq = self.find_element(By.ID, "unqualifiedBuyBox")
            return 0
        except NoSuchElementException:
            pass

        return 1
             
        
    def get_merchant_info(self):
            merchant_info_div = WebDriverWait(self, 10).until(
                ec.visibility_of_element_located((By.ID, 'merchant-info'))
            )
            merchant_info = merchant_info_div.find_element(By.TAG_NAME, 'a').text
            return merchant_info

    def get_ETrade_price(self):
            offer_divs = self.find_elements(By.CSS_SELECTOR, 'div.a-box.mbc-offer-row.pa_mbc_on_amazon_offer')
            for offer_div in offer_divs:
                merchant_name_element = offer_div.find_element(By.CSS_SELECTOR, 'span.mbcMerchantName')
                merchant_name = merchant_name_element.text.strip()

                if merchant_name == "ETrade Online":
                    price_element_ET = offer_div.find_element(By.CSS_SELECTOR, 'span.a-size-medium.a-color-price')
                    price_ET = price_element_ET.text.strip()
                    return price_ET
                

            return None