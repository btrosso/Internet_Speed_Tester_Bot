import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        time.sleep(5)
        go_button.click()
        time.sleep(60)
        try:
            close_popup = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
            close_popup.click()
        except NoSuchElementException:
            print("Popup not present yet.")
        else:
            download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            upload_speed = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
            print(f"Download speed: {download_speed.text}")
            print(f"Upload speed: {upload_speed.text}")


    def tweet_at_provider(self):
        # sign in to twitter
        self.driver.get("https://twitter.com/")
        time.sleep(5)
        sign_in_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in_btn.click()
        time.sleep(5)
        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys(os.environ['TWITTER_EMAIL'])
        time.sleep(5)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        next_btn.click()
        time.sleep(5)
        try:
            pass_input = self.driver.find_element(By.NAME, "password")
            pass_input.send_keys(os.environ['TWITTER_PASSWORD'])
            time.sleep(5)
            login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
            login_btn.click()
            time.sleep(5)
        except NoSuchElementException:
            user_input = self.driver.find_element(By.CLASS_NAME, "text")
            user_input.send_keys(os.environ['TWITTER_USERNAME'])
            alt_next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
            alt_next_btn.click()
            time.sleep(5)
            pass_input = self.driver.find_element(By.NAME, "password")
            pass_input.send_keys(os.environ['TWITTER_PASSWORD'])
            time.sleep(5)
            alt_login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
            alt_login_btn.click()
            time.sleep(5)

        tweet = self.driver.find_element(By.CLASS_NAME, "DraftEditor-root")
        tweet.send_keys("Hello")

