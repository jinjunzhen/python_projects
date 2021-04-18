##   "https://chromedriver.chromium.org/downloads" ----->   download chrome driver
##   chrome driver is a bridge connect with chrome and pothon program

from selenium import webdriver

CHROME_DRIVER_PATH = "/Users/jinjunzhen/development/chromedriver"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://www.python.org/")


dict_event = {}
for i in range(0,5):
    dict_temp = {}
    time1 = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time').text
    event1 = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a').text
    dict_temp['time'] = time1
    dict_temp['name'] = event1
    dict_event[i] = dict_temp

print(dict_event)

driver.close()   #close single tab
driver.quit()  #quit the entire program

