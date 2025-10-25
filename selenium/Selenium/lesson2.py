from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
from  webdriver_manager.chrome import  ChromeDriverManager
import time

# Configure the options.
opts = Options()
# opts.add_argument("--headless=new")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")

# Configure the service.
service = Service(ChromeDriverManager().install())

# Create the browser instance.
browser = webdriver.Chrome(service=service, options=opts)

# Let's work on a function to login into "https://www.saucedemo.com/"
def login():
    # First : let load into the page.
    browser.get("https://www.saucedemo.com/")

    # Let's get the necessary field for login.
    # 1. Username field
    # 2. Password field
    # 3. Login button

    username_field = browser.find_element(By.ID, "user-name")
    password_field = browser.find_element(By.ID, "password")

    login_btn = browser.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")

    login_btn.click()


# login()

# time.sleep(10)
# Function to open YouTube and make a search.
def search_youtube():
    browser.get("https://youtube.com")

    time.sleep(10)

    # Get the search field.
    search_field = browser.find_element(By.CSS_SELECTOR, "form.ytSearchboxComponentSearchForm input[name='search_query']")

    search_btn = browser.find_element(By.XPATH, "//button[contains(@class, 'ytSearchboxComponentSearchButton') and @title='Search']")
    # Enter the search text.
    search_field.send_keys("Mr Beast latest video")

    search_btn.click()

search_youtube()

time.sleep(60)