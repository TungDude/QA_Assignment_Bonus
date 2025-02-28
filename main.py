from selenium.webdriver.common.by import By
from src.DriverController import DriverController

def test_search_sertis():
    google_url = "https://www.google.co.th/?hl=en"
    driver = DriverController(google_url)
    
    # Landing on google search page
    driver.load_page()
    
    # Search for Sertis
    driver.search_box_input(
        element_function = lambda driver: (
            driver.find_element(By.CSS_SELECTOR, "textarea[title='Search']")
        ),
        input = "Sertis"
    ) 
    
    # Validate the display of Sertis website
    driver.validate_search_result("https://www.sertiscorp.com/")
    driver.quit()
    

if __name__ == "__main__":
    test_search_sertis()