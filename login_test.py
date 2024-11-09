from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the login page
driver.get("https://demo.opencart.com/index.php?route=account/login")

# Find the email (username) field and enter a value
email_field = driver.find_element(By.ID, "input-email")
email_field.send_keys("test@example.com")

# Find the password field and enter a value
password_field = driver.find_element(By.ID, "input-password")
password_field.send_keys("password123")

# Find the login button and click it
login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
login_button.click()

# Check if "My Account" appears in the title of the page
assert "My Account" in driver.title
print("Login Test Passed")

# Close the browser after test
driver.quit()
