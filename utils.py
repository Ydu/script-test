# utils.py

import pytest
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def setup():
	chrome_options = Options()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("--headless")  # Run in headless mode
	# chrome_options.add_argument("--disable-gpu")  # Disable GPU usage (usually recommended)
	# chrome_options.add_argument("--window-size=1920,1080")

	# Setup: Initialize the WebDriver and open the browser
	driver = webdriver.Chrome(options=chrome_options)
	driver.maximize_window()
	yield driver
	# Teardown: Close the browser after the test
	driver.quit()

def login(setup):
	driver = setup
	
	# Step 1: Navigate to the website
	driver.get("https://test.app.101gen.ai/login")  
	wait = WebDriverWait(driver, timeout=10)
	
	# Step 2: Locate and interact with the form fields
	email_field = driver.find_element(By.XPATH, "//input[@name='username']")  
	password_field = driver.find_element(By.XPATH, "//input[@name='password']")  
	
	# Step 3: Input data into the fields
	email_field.send_keys("root@101gen.ai")
	password_field.send_keys("Sdi3FdrDgAj2pKv")

	# Step 4: Submit the form
	submit_button = wait.until(
		EC.element_to_be_clickable((By.XPATH, "//span[text()='Login']/.."))
	)
	submit_button.click()
	wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Welcome to 101GenAI!']")))
	assert driver.current_url == "https://test.app.101gen.ai/dashboard", "Did not reach the correct URL."
	time.sleep(5)