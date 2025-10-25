from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Configure options
options = Options()
# options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--diable-shm-dev-usage")


# Configure the service.
service = Service(ChromeDriverManager().install())

# Get the browser instance.
browser = webdriver.Chrome(service=service, options=options)

def fill_form_and_check_box():

    browser.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Get the input fields.
    text_input = browser.find_element(By.CSS_SELECTOR, "#my-text-id")
    password_input = browser.find_element(By.XPATH, "//input[@class='form-control' and @name='my-password']")
    text_area = browser.find_element(By.XPATH, "//textarea[@class='form-control' and @name='my-textarea']")

    checkbox = browser.find_element(By.CSS_SELECTOR, "input#my-check-1")
    default_checkbox = browser.find_element(By.CSS_SELECTOR, "input#my-check-2")
    radio_btn = browser.find_element(
        By.XPATH, "//input[@id='my-radio-2' and @class='form-check-input' and @type='radio']")
    submit_btn = browser.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-outline-prim')]")

    # Add text to the text input fields.
    text_input.send_keys("Stephen Muiru")
    password_input.send_keys("MySupperPassword!!")
    text_area.send_keys("I have no comments at the moment.")

    # Mark the checkboxes and the radio box
    checkbox.click()

    if checkbox.is_selected():
        print("The checkbox has been selected")

    if default_checkbox.is_selected():
        print("The second radio box has been selected")
    else:
        print("The second radio box has not been selected yet.")
        default_checkbox.click()

    radio_btn.click()

    sleep(10)

    submit_btn.submit()

    sleep(10)


def main():
    fill_form_and_check_box()

if __name__ == "__main__":
    main()