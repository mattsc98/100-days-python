from selenium import webdriver
from selenium.webdriver.common.by import By

LINKEDIN_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3724099189&f_AL=true&keywords=Automation%20Engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER'

# Set the Chromedriver path (replace with your path)
chromedriver_path = r'C:\Users\matthew.schembri\OneDrive - Gain Changer\Documents\Automation\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Initialize the webdriver
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get(LINKEDIN_URL)


driver.close()