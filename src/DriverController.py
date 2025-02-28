from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import random
import time

class DriverController():
    def __init__(self, url):
        self.driver = self.init_driver()
        self.url = url
    
    def init_driver(self):
        """Set up the Selenium WebDriver."""
        # Set up Chrome options
        options = Options()
        # options.add_argument("--headless")  # Optional: Run in headless mode
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)
        
        return driver
    
    def screenshot(self, filename):
        screenshots_folder_path = "screenshots"
    
        if not os.path.exists(screenshots_folder_path):
            os.makedirs(screenshots_folder_path)
            
        self.driver.save_screenshot(os.path.join(screenshots_folder_path, filename))
    
    def random_sleep(self, min_duration=0.8, max_duration=3.1):
        random_duration = random.uniform(min_duration, max_duration)
        time.sleep(random_duration)
    
    def quit(self):
        self.driver.quit()
    
    def load_page(self):
        self.driver.get(self.url)
        self.screenshot("1_google.png")
        
    def search_box_input(self, element_function, input):
        search_box = WebDriverWait(self.driver, 10).until(
            element_function
        )
        
        keys_to_send = list(input)
        for ch in keys_to_send:
            self.random_sleep(0.5, 0.8)
            search_box.send_keys(ch)

        # Get value inside the search box
        entered_text = search_box.get_attribute("value")

        # Check if the entered text is correct
        if entered_text == input:
            print(f"Test Passed: '{input}' is in the search box")
        else:
            print(f"Test Failed: '{entered_text}' is in the search box (Expected: '{input}')")

        self.screenshot(f"2_{input}_seach_box.png")
        self.random_sleep()
        search_box.send_keys(Keys.RETURN)
    
    def validate_search_result(self, url_to_find):
        # Search results container
        search_results = self.driver.find_element(By.ID, "search")
        
        # Find all <a> tags inside the search div
        links = search_results.find_elements(By.TAG_NAME, "a")
        
        # Check for Sertis url
        for link in links:
            href = link.get_attribute("href")
            if href == url_to_find:  # Only print and exit if href matches the target url
                print(f"Test Passed: '{url_to_find}' found in the search page")
                break
        else:
            print(f"Test Failed: '{url_to_find}' not found")
                
        self.screenshot("3_search_results.png")