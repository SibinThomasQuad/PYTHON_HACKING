from selenium import webdriver
from PIL import Image
import io  # Import the 'io' module

# Create a Firefox WebDriver instance
driver = webdriver.Firefox()

# Navigate to the webpage you want to capture
url = "https://example.com"  # Replace with the URL of the webpage you want to capture
driver.get(url)

# Wait for the page to load completely (you can adjust the wait time as needed)
driver.implicitly_wait(10)

# Get the height of the entire page
page_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

# Set the window size to capture the entire page
driver.set_window_size(driver.get_window_rect()['width'], page_height)

# Capture the screenshot of the entire page
screenshot = driver.get_screenshot_as_png()

# Convert the screenshot to an image
img = Image.open(io.BytesIO(screenshot))

# Save the full-length screenshot
img.save("full_page_screenshot.png")

# Close the WebDriver
driver.quit()
