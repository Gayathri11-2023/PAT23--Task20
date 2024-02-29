from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Cowin:
    url = "https://www.cowin.gov.in/"
    faq = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"
    partners = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Get the Url to opened and maximize it
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
    # This function is used to get the window id and print the id on the console
    def get_window_id(self):
        parent_window_handle = self.driver.current_window_handle
        print(parent_window_handle)
        all_window_handles = self.driver.window_handles
        print(all_window_handles)
    # close the windows from partner window to main window
    def close_window(self):
        second_window = self.driver.window_handles[2]
        self.driver.switch_to.window(second_window)
        self.driver.close()
        time.sleep(1)
        third_window = self.driver.window_handles[1]
        self.driver.switch_to.window(third_window)
        self.driver.close()
        time.sleep(1)
        third_window = self.driver.window_handles[0]
        self.driver.switch_to.window(third_window)
        self.driver.close()
        time.sleep(1)

    # Open the FAQ window on the sepearate tab
    def faq_window(self):
        self.driver.find_element(by=By.XPATH, value=self.faq).click()
        time.sleep(3)
    # Open the Partners window on the seperate tab
    def partners_window(self):
        self.driver.find_element(by=By.XPATH, value=self.partners).click()
        time.sleep(3)
    # quit the driver
    def quit(self):
        self.driver.quit()

# create the object for class Cowin()
obj = Cowin()
obj.boot()
obj.faq_window()
obj.partners_window()
obj.get_window_id()
obj.close_window()
obj.quit()