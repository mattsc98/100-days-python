from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class ZillowData:
    def __init__(self, url, chrome_driver):
        chrome_service = ChromeService(executable_path=chrome_driver)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without a GUI)

        # Create a WebDriver instance
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        self.driver.get(url)

        # Wait for the page to load (you can adjust the timeout as needed)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.presence_of_element_located((By.ID, 'grid-search-results')))

def get_data(self):
    try:
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # Extract and process data from the soup object as needed
        listings = soup.find_all('article', class_='list-card')
        
        for listing in listings:
            # Extract data from each listing, e.g., title, price, address, etc.
            title = listing.find('a', class_='list-card-link').text.strip()
            price = listing.find('div', class_='list-card-price').text.strip()
            address = listing.find('address').text.strip()
            
            # Print or store the extracted data as needed
            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Address: {address}")
            print('-' * 30)

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        self.close_driver()

    def close_driver(self):
        self.driver.quit()
