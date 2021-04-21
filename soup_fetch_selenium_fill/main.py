import requests
import os
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

FILL_IN_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSe6lAosmVKRF8Cv-CfP2FvNDnwyVwfJw3hvbUYpygxYjhfJWg/viewform?usp=sf_link'

zillow_list = []


#################  part 1 fetch data from zillow with beautiful_soup

url = 'https://www.zillow.com/san-francisco-ca/apartments/2-_beds/1.5-_baths/paymenta_sort/' \
      '?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Franc' \
      'isco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.62774334020662%2C%22east%22%3A-' \
      '122.27068767614412%2C%22south%22%3A37.62711230761565%2C%22north%22%3A37.83103745990713%' \
      '7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%' \
      '5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%' \
      '3A797132%2C%22max%22%3A919768%7D%2C%22mp%22%3A%7B%22min%22%3A2600%2C%22max%22%3A3000%' \
      '7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22baths%22%3A%7B%22min%22%3A1.5%7D%2C%22sort%' \
      '22%3A%7B%22value%22%3A%22paymenta%22%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%' \
      '22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%' \
      '22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%' \
      '22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3A' \
      'false%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%' \
      '7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%' \
      '22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%' \
      '22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22sf%22%3A%7B%' \
      '22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja;q=0.6,zh-TW;q=0.5"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
# with open("output1.html", "w") as file1:
#     file1.write(str(soup))


ul = soup.find('ul', class_='photo-cards photo-cards_wow photo-cards_short')

for li in ul.find_all('li'):
    dict_temp = {}
    if li.find('div', class_='list-card-price') != None:
        dict_temp['price'] = li.find('div', class_='list-card-price').text
    if li.find('address', class_='list-card-addr') != None:
        dict_temp['address'] = li.find('address', class_='list-card-addr').text
    if li.find('a') != None:
        dict_temp['link'] = li.find('a').get('href')
    if bool(dict_temp):
        zillow_list.append(dict_temp)

print(zillow_list)

##############################   part 2  fill into google form with Selenium


driver = webdriver.Chrome(executable_path=os.environ['chrome_driver'])

driver.get(FILL_IN_LINK)
sleep(1)
for zillow_item in zillow_list:
    new_address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    new_address.send_keys(zillow_item['address'])
    new_price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    new_price.send_keys(zillow_item['price'])
    new_link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    new_link.send_keys(zillow_item['link'])
    new_submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    new_submit.click()
    sleep(2)
    new_a_link = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_a_link.click()
    sleep(1)

driver.close()




