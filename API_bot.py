from selenium import webdriver
from time import sleep

#Use your own username and password for this
username = "your_username"
password = "your_password"
 
class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver_win32/chromedriver')

    def login(self):
        self.driver.get('https://bumble.com/app')
        sleep(10)   
        fb_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div/div[2]/div/span/span[2]')
        fb_btn.click()
        sleep(5)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        passw = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passw.send_keys(password)
        login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()
        sleep(10)
        self.driver.switch_to_window(self.driver.window_handles[0])
        
        for i in range(5):
            self.like()
            sleep(2)
            self.pass_()
            sleep(2)
    #to swipe right to the profile you see    
    def like(self):
        like_btn = bot.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
        like_btn.click()
    #to swipe left to the profile you see    
    def pass_(self):
        #xpath may need to be changed
        pass_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')
        pass_btn.click()

bot = BumbleBot()
bot.login()

