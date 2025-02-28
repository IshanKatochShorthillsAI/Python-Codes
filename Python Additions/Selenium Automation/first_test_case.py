from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/snap/bin/firefox.geckodriver")
driver = webdriver.Firefox(service=serv_obj)
driver.implicitly_wait(20)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(
    By.CSS_SELECTOR,
    ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button",
).click()

act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Test Passed")
else:
    print("Test Failed")
