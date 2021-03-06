import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = 'jinjunzhen@yahoo.com'
FB_PASSWORD = os.environ['fb_pw']

chrome_driver_path = "/Users/jinjunzhen/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="u-1554866805"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
cookies = driver.find_element_by_xpath('//*[@id="u-1554866805"]/div/div[2]/div/div/div[1]/button')
cookies.click()
notifications_button = driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div/div/div[3]/button[1]')
notifications_button.click()
sleep(6)
no_thanks_btn = driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div[1]/button')
no_thanks_btn.click()

sleep(8)
main_screen = driver.find_element_by_xpath('//*[@id="u-1554866805"]/div/div[1]/div/main/div[1]/div/div')
main_screen.click()


#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    # try:
    print(len(driver.window_handles))
    print("called")
    xpath = '//*[@id="u-1554866805"]/div/div[1]/div/div/main/div/div[1]/div[1]/div[2]/div[4]/button'
    like_btn = driver.find_element_by_xpath(xpath)
    like_btn.click()


    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    # except ElementClickInterceptedException:
    #     try:
    #         match_popup = driver.find_element_by_css_selector(".itsAMatch a")
    #         match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        # except NoSuchElementException:
        #     sleep(2)

driver.quit()