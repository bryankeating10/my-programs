import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to Microsoft Edge WebDriver
EDGE_DRIVER_PATH = "C:/path/to/msedgedriver.exe"  # Change this to your actual path

# Sample question templates
question_templates = [
    "What is the history of {}?",
    "How does {} work?",
    "Why is {} important?",
    "What are the benefits of {}?",
    "Can you explain {}?",
    "Who discovered {}?",
    "Where can I learn more about {}?",
    "When did {} happen?",
    "Is {} real?",
    "Could {} be dangerous?"
]

# Random topics for question generation
topics = [
    "quantum physics", "artificial intelligence", "black holes", "climate change",
    "ancient Rome", "Bitcoin", "machine learning", "space travel",
    "psychology", "deep sea creatures", "neural networks", "medieval castles"
]

# Initialize Edge WebDriver
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service)

# Perform 30 searches
for i in range(30):
    # Generate a random question
    question = random.choice(question_templates).format(random.choice(topics))
    print(f"Searching for: {question}")

    try:
        # Open Bing
        driver.get("https://www.bing.com")

        # Locate the search box, enter the query, and hit Enter
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(question)
        search_box.send_keys(Keys.RETURN)

        # Wait for search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.b_algo a"))
        )

        # Click the first search result
        first_result = driver.find_element(By.CSS_SELECTOR, "li.b_algo a")
        first_result.click()

        # Wait for 10 seconds
        time.sleep(10)

        # Close the current tab
        driver.close()

        # Open a new Edge window for the next search
        driver = webdriver.Edge(service=service)

    except Exception as e:
        print(f"Error on search {i+1}: {e}")
        break

# Close browser after all searches
driver.quit()