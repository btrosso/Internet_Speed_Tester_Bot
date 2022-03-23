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
        self.download_speed = ""
        self.upload_speed = ""

    def get_internet_speed(self):
        """
        Method runs internet speedtest and saves the upload and download speeds to this class.
        :return:
        """
        # go to the speed test page and start the test
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[1]/a')
        time.sleep(5)
        go_button.click()
        time.sleep(60)
        try:
            # try to close the popup window
            close_popup = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                             'div[3]/div[3]/div/div[8]/div/a')
            close_popup.click()
        except NoSuchElementException:
            print("Popup not present yet.")
        else:
            # get the download and upload speed
            self.download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/'
                                                                     'div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/'
                                                                     'div[1]/div[2]/div/div[2]/span').text
            self.upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                                   'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/'
                                                                   'div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        """
        This method will log in to Twitter. Currently, it posts a tweet with your internet speed stats.
        :return:
        """
        # sign in to twitter
        self.driver.get("https://twitter.com/")
        time.sleep(5)
        sign_in_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/'
                                                         'div[1]/div/div[3]/div[5]/a/div')
        sign_in_btn.click()
        time.sleep(5)
        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys(os.environ['TWITTER_EMAIL'])
        time.sleep(5)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                                      'div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        next_btn.click()
        time.sleep(5)
        user_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                                                        'div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/'
                                                        'div/input')
        user_input.send_keys(os.environ['TWITTER_USERNAME'])
        alt_next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                                                          'div/div/div[2]/div[2]/div[2]/div/div/div/div')
        alt_next_btn.click()
        time.sleep(5)
        pass_input = self.driver.find_element(By.NAME, "password")
        pass_input.send_keys(os.environ['TWITTER_PASSWORD'])
        time.sleep(5)
        alt_login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                                                           'div/div/div[2]/div[2]/div[2]/div/div[1]/div')
        alt_login_btn.click()
        time.sleep(5)

        # compose the tweet
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
                                                   'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/'
                                                   'div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/'
                                                   'div/div/div')
        tweet.send_keys(f"My Internet Speed Test shows:\nDownload Speed: {self.download_speed}\n"
                        f"Upload Speed: {self.upload_speed}")
        time.sleep(5)
        # send it
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                       'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/'
                                                       'div/div[2]/div[3]')
        tweet_btn.click()

        self.driver.quit()
