from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver_path = "/Users/jinjunzhen/development/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
target_list = driver.find_elements_by_css_selector(".form-signin .form-control")
target_list[0].send_keys("Jinjun")
target_list[1].send_keys("Zhen")
target_list[2].send_keys("jinjunzhen@yahoo.com")

sign_up_button = driver.find_element_by_css_selector(".form-signin .btn")
sign_up_button.click()

driver.close()


