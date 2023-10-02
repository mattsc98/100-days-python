from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time

# Load environment variables from the .env file
load_dotenv("Day 49/.env")

LINKEDIN_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3724099189&f_AL=true&keywords=Automation%20Engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER'
ACCOUNT_EMAIL  = 'mattsc98@gmail.com'
ACCOUNT_PASSWORD  = os.getenv("PASSWORD")
PHONE = os.getenv("NUMBER")


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

# Set the Chromedriver path (replace with your path)
chromedriver_path = r'C:\Users\matthew.schembri\OneDrive - Gain Changer\Documents\Automation\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Initialize the webdriver
driver = webdriver.Chrome(executable_path=chromedriver_path)
wait = WebDriverWait(driver, 10)  
driver.get(LINKEDIN_URL)


# Click the Sign In button
sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')))
sign_in_button.click()

# Fill in the email
email = wait.until(EC.presence_of_element_located((By.ID, 'username')))
email.send_keys(ACCOUNT_EMAIL )

# Fill in the password
password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
password.send_keys(ACCOUNT_PASSWORD )

# Click the login button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')))
login_button.click()

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()


