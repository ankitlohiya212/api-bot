from selenium import webdriver
from time import sleep

#Use your own username and password for this
username = "your_username"
password = "your_password"


class PDF_download():
    def __init__(self, book_name):
        self.driver = webdriver.Chrome('path/to/chromedriver_win32/chromedriver')
        self.book_name = book_name
    def download(self):
        try:
            self.book_search = self.book_name.replace(' ','+')
            self.driver.get(f"https://www.pdfdrive.com/search?q={self.book_search}&pagecount=&pubyear=&searchin=")
            sleep(3)
            for i in range(1, 11):
                found = 0
                print(i)
                book = self.driver.find_element_by_xpath(f'/html/body/div[3]/div[1]/div[1]/div[4]/ul/li[{i}]/div/div/div[2]/a/h2')
                #download if the PDF name starts with the title searched for
                if book.text.capitalize().startswith(self.book_name.capitalize()):
                    book.click()
                    break
                    found = 1
                #If none of the available PDFs starts with the name searched
                if i == 10 and not found:
                    book = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[4]/ul/li[1]/div/div/div[2]/a/h2')
                    book.click()
                
            sleep(3)
            download1 = self.driver.find_element_by_xpath('//*[@id="download-button-link"]')
            download1.click()
            sleep(15)
            try:
                download2 = self.driver.find_element_by_xpath('//*[@id="alternatives"]/div[1]/div/a')
                download2.click()
            except:
                download2 = self.driver.find_element_by_xpath('//*[@id="alternatives"]/div[1]/a')
                download2.click()
                try:
                    self.driver.switch_to_window(self.driver.window_handles[1])
                    sleep(0)
                    download3 = self.driver.find_element_by_xpath('//*[@id="icon"]/iron-icon')
                    download3.click()
                except:
                    pass
        except:
            try:
                self.dismiss_popup()
                self.download()
            except:
                self.download()
    #To Dismiss Popups
    def dismiss_popup(self):
        cancel = self.driver.find_element_by_xpath('//*[@id="pdfdriveAlerts"]/div/div/div/i')
        cancel.click()

book_name = 'Divergent'
bot = PDF_download(book_name)
bot.download()

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

