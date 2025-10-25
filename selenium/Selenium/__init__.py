from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def first_lesson():
    # Driver options.
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Create an instance on the service.
    service =  Service(ChromeDriverManager().install())


    # Create the browser instance.
    browser = webdriver.Chrome(service=service, options=options)

    # Open a page.

    browser.get("https://google.com")

    print(browser.title)
    print(browser.current_url)

    time.sleep(10)