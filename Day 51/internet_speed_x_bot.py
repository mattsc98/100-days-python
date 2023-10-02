from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InternetSpeedTwitterBot():
    def __init__(self, chromedriver_path):
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)
        self.wait = WebDriverWait(self.driver, 60)          
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        
        accept_wait = (By.ID, 'onetrust-accept-btn-handler')
        accept = self.wait.until(EC.element_to_be_clickable(accept_wait))
        accept.click()
                
        go_wait = (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')                
        go_button = self.wait.until(EC.element_to_be_clickable(go_wait))
        go_button.click()
        
        download_speed_xpath = '//*[@class="result-container-speed result-container-speed-active"]//*[@class="result-data-large number result-data-value download-speed"]'
        download_speed_element = self.wait.until(EC.presence_of_element_located((By.XPATH, download_speed_xpath)))
        self.down = download_speed_element.text
        
        upload_speed_xpath = '//*[@class="result-container-speed result-container-speed-active"]//*[@class="result-data-large number result-data-value upload-speed"]'
        upload_speed_element = self.wait.until(EC.presence_of_element_located((By.XPATH, upload_speed_xpath)))
        self.up = upload_speed_element.text        
        
        
        print(f'download speed: {self.down}')
        print(f'upload speed: {self.up}')
        

        
    
    def tweet_at_provider(self, email, password):
        self.driver.get('https://twitter.com/i/flow/login')
        
        email_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]')))
        email_input.send_keys(email)
        
        next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')))
        next_button.click()
        
        password_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        password_input.send_keys(password)
        
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')))
        login_button.click()
        
        accept_cookies = (By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div/span/span')                
        accept_cookies_button = self.wait.until(EC.element_to_be_clickable(accept_cookies))
        accept_cookies_button.click()  
        
        tweet_box_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
        tweet_box_element = self.wait.until(EC.presence_of_element_located((By.XPATH, tweet_box_xpath)))
        tweet_box_element.send_keys(f"Why is my download at {self.down} and my upload at {self.up}?")
        
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div')
        post_button.click()
        
        print('ready')