# pages/base_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
class BasePage:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def initiation_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except:
            print("ERROR : URL is incorrect/Network Error")
            return False

    def enter_text(self, element_id, text):
        self.driver.find_element(By.XPATH, element_id).send_keys(text)

    def click_element(self, element):
        self.driver.find_element(By.XPATH, element).click()

    def is_element_present(self, element_id):
        return bool(self.driver.find_element(By.XPATH, element_id))



    def shutdown(self):
        if self.initiation_function():
            return self.driver.quit()
        else:
            return False

