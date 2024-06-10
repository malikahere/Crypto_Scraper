# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# class CoinMarketCap:
#     BASE_URL = 'https://coinmarketcap.com/'

#     def __init__(self):
#         self.driver = self._initialize_driver()

#     def _initialize_driver(self):
#         service = Service(ChromeDriverManager().install())
#         return webdriver.Chrome(service=service)

#     def make_request(self, url):
#         self.driver.get(url)
#         # Wait for dynamic content to load (if any)
#         time.sleep(3)
#         return self.driver.page_source

#     def scrape_data(self, coin_name):
#         url = f'{self.BASE_URL}currencies/{coin_name}/'
#         html_content = self.make_request(url)
#         if html_content:
#             data = {
#                 'price': self.safe_extract('div[class*="priceValue"]', html_content),
#                 'price_change': self.safe_extract('span[class*="price-change"]', html_content),
#                 'market_cap': self.safe_extract('div[class*="market-cap"]', html_content),
#                 'market_cap_rank': self.safe_extract('div[class*="cmc-details-panel-stats"] div:contains("Market Cap Rank") + div', html_content),
#                 'volume': self.safe_extract('div[class*="volume"]', html_content),
#                 'volume_rank': self.safe_extract('div[class*="cmc-details-panel-stats"] div:contains("Volume Rank") + div', html_content),
#                 'volume_change': self.safe_extract('div[class*="volume"]', html_content),  # Update this selector accordingly
#                 'circulating_supply': self.safe_extract('div[class*="circulating-supply"]', html_content),
#                 'total_supply': self.safe_extract('div[class*="total-supply"]', html_content),
#                 'diluted_market_cap': self.safe_extract('div[class*="diluted-market-cap"]', html_content),
#                 # Add more fields as necessary
#             }

#             return data
#         return None

#     def safe_extract(self, selector, html_content):
#         element = self.driver.find_element_by_css_selector(selector)
#         return element.text.strip() if element else None

#     def close_driver(self):
#         self.driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CoinMarketCap:
    BASE_URL = 'https://coinmarketcap.com/'

    def __init__(self):
        self.driver = self._initialize_driver()

    def _initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)

    def scrape_data(self,coin_name):
        url = f'{self.BASE_URL}currencies/{coin_name}/'
        self.driver.get(url)
        
        try:
            # Wait for price and market cap elements to be present
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class*="priceValue"]'))
            )
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class*="market-cap"]'))
            )

            # Extract data using CSS selectors
            data = {
                'price': self.safe_extract('div[class*="priceValue"]'),
                'price_change': self.safe_extract('span[class*="price-change"]'),
                'market_cap': self.safe_extract('div[class*="market-cap"]'),
                'market_cap_rank': self.safe_extract('div[class*="cmc-details-panel-stats"] div:contains("Market Cap Rank") + div'),
                'volume': self.safe_extract('div[class*="volume"]'),
                'volume_rank': self.safe_extract('div[class*="cmc-details-panel-stats"] div:contains("Volume Rank") + div'),
                'volume_change': self.safe_extract('div[class*="volume"]'),  # Update this selector accordingly
                'circulating_supply': self.safe_extract('div[class*="circulating-supply"]'),
                'total_supply': self.safe_extract('div[class*="total-supply"]'),
                'diluted_market_cap': self.safe_extract('div[class*="diluted-market-cap"]'),
                # Add more fields as necessary
            }

            return data
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    def safe_extract(self, selector):
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        return element.text.strip() if element else None

    def close_driver(self):
        self.driver.quit()
