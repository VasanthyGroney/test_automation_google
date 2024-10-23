import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Instantiate a WebDriver Object
driver = webdriver.Chrome()

try:
    # Navigate to Google
    print("Navigating to Google...")
    driver.get("https://www.google.com")

    # Find the search bar input element and send the search term "cats"
    print("Waiting for the search box...")
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    print("Sending search term...")
    search_box.send_keys("cats")

    # Wait for 3 seconds
    print("Waiting for 3 seconds...")
    time.sleep(3)

    # Print the title of the document
    print("Browser Title:", driver.title)

except TimeoutException:
    print("The search box did not load in time.")
except NoSuchElementException:
    print("The search box element could not be found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Quit the browser
    print("Quitting the browser...")
    driver.quit()
