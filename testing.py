from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import random
import sys
import time
import string
from selenium.webdriver.common.keys import Keys
import requests
class Test_module:
    def __init__(self):
        self.google = "https://www.google.com/"
        self.base_url = "http://localhost:8000"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.COMMAND_OR_CONTROL = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
    def open_url(self):
        #self.driver.get("http://stackoverflow.com/questions/6509628/webdriver-get-http-response-code")
        self.driver.get(self.base_url)

    def random_char(self,y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

    def checking_links(self):
        try:
            time.sleep(1)
            p = self.driver.find_element_by_link_text("Maharashtra").click()
            time.sleep(2)
            p = self.driver.find_element_by_link_text("India").click()
            time.sleep(2)
            p = self.driver.find_element_by_name('World').click()
            time.sleep(2)
            print('all links are working')
        except Exception as e:
            print('test case failed:'+str(e))
    def checking_api(self):
        try:
            r = requests.head("https://www.worldometers.info/coronavirus/")
            print(r.status_code)
            if(r.status_code==200):
                print('test case 3 is passed api working properly')
        except requests.ConnectionError:
            print("test case 3 is failed api working properly")
    def checking_images(self):
        try:
            r = requests.head("http://127.0.0.1:8000/static/graphs/top.png")
            print(r.status_code)
            if(r.status_code==200):
                print('test case 2 is passed')
            else:
                print('test case 2 is failed , image not found')
        except requests.ConnectionError:
            print("_")

            
if __name__ == '__main__':
    bot = Test_module()
    bot.open_url()
    bot.checking_links()
    bot.checking_api()
    bot.checking_images()



