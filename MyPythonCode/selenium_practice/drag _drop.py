from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Replace with your driver, e.g., webdriver.Firefox() if using Firefox

# Open the target webpage
driver.get("https://example.com")  # Replace with the URL of the page containing drag-and-drop elements

# Maximize the browser window
driver.maximize_window()

time.sleep(2)  # Wait for the page to load (adjust based on page load time)

try:
    # Locate the source element (the element to drag)
    source_element = driver.find_element(By.ID, "source")  # Replace 'source' with the actual ID or selector

    # Locate the target element (the element to drop into)
    target_element = driver.find_element(By.ID, "target")  # Replace 'target' with the actual ID or selector

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Perform drag and drop
    actions.drag_and_drop(source_element, target_element).perform()
    print("Drag and drop action completed.")

    # Perform mouse hover over a specific element (if needed)
    hover_element = driver.find_element(By.ID, "hover")  # Replace 'hover' with the actual ID or selector
    actions.move_to_element(hover_element).perform()
    print("Mouse hover action completed.")

    time.sleep(2)  # Pause to observe actions (optional)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed.")
