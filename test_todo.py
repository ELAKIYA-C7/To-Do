from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Open the local index.html (adjust path if needed)
driver.get("file:///C:/path/to/your/index.html")  # Use absolute path

# Find input box and add button
task_input = driver.find_element(By.ID, "taskInput")
add_button = driver.find_element(By.TAG_NAME, "button")

# Type a task and click Add
task_input.send_keys("Test Task")
add_button.click()

time.sleep(1)  # wait for JS to update DOM

# Check if task was added
tasks = driver.find_elements(By.TAG_NAME, "li")
if any("Test Task" in task.text for task in tasks):
    print("Test Passed: Task added successfully!")
else:
    print("Test Failed: Task not added.")

driver.quit()