from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
class Downloadimages:
    def __init__(self, url="https://labour.gov.in/"):
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
    # close the popup body
    def close_popup_body(self):
        self.getElementByXpath('//*[@id="popup"]/div[2]/button').click()
        sleep(4)
        print("Success the popup body is closed!")
    # click on the photo Gallery
    def clickonphotogallery(self):
        mediaElement = self.getElementByXpath("//*[@id=\"nav\"]/li[10]/a")
        self.actionChains.move_to_element(mediaElement).perform()
        sleep(3)
        self.getElementByXpath("//*[@id=\"nav\"]/li[10]/ul/li[2]/a").click()
        sleep(3)
        print("Success, The photogallery is clicked")
    #  To download the photos from the photo gallery
    def downloadphotos(self):
        sleep(2)
        for i in range(1, 11):
            xpath = f'//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[{i}]/td[1]/div[1]/div/img'
            url = self.getElementByXpath(xpath).get_attribute("src")
            print("The url of image is:", url)
            response = requests.get(url)
            if response.status_code == 200:
                filepath = f"Images/image {i}.png"
                f = open(filepath, "wb")
                f.write(response.content)
                f.close()
                print(f"Image{i} is successfully downloaded")
            else:
                print("error")
if __name__ == "__main__":
    obj = Downloadimages()
    obj.boot()
    obj.close_popup_body()
    obj.clickonphotogallery()
    obj.downloadphotos()
    obj.quit()
