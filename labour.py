from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests

class Labour:
    def __init__(self, url ="https://labour.gov.in/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.actionChains = ActionChains(self.driver)
    def boot(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()
        sleep(2)
    def quit(self):
        self.driver.quit()
    def getElementByXpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)
     # close the pop up body
    def close_popup_body(self):
        self.getElementByXpath("//*[@id=\"popup\"]/div[2]/button").click()
        sleep(4)
        print("Success the popup body is closed!")
    # Click on the monthly progress report from the document menu
    def click_monthly_progress_report(self):
        documentelement = self.getElementByXpath("/html/body/div[1]/nav/div/div/div/ul/li[7]/a")
        self.actionChains.move_to_element(documentelement).perform()
        sleep(4)
        self.getElementByXpath("/html/body/div[1]/nav/div/div/div/ul/li[7]/ul/li[2]/a").click()
        print("Success click on the progress report")
        sleep(4)
    # Accept the alert and open the documents in seperate tab
    def open_documents(self):
        self.getElementByXpath("/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a").click()
        self.driver.switch_to.alert.accept()
        sleep(2)
        print("success The document is opened")
    # By using the file handling method to download the document 
    def download_document(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        print("The URL of the document: ", url)
        response = requests.get(url)
        if response.status_code == 200:
            filepath = "MonthlyProgressReport.pdf"
            f = open(filepath,  "wb")
            f.write(response.content)
            f.close()
        else:
            print("Error")
if __name__ == "__main__":
    obj = Labour()
    obj.boot()
    obj.close_popup_body()
    obj.click_monthly_progress_report()
    obj.open_documents()
    obj.download_document()
    obj.quit()







