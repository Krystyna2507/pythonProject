from webbrowser import Chrome

import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
from selenium.webdriver import Chrome


@pytest.fixture(scope="module")
def driver():
    print("Init driver")
    driver = Chrome()
    yield driver
    print("Quit driver")
    driver.quit()


def test_reg_errortext(driver):

'''
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." in driver.page_source
driver.close()
'''
'''
# залогінитись:
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
driver.maximize_window()
btnsgn = driver.find_element(By.XPATH,
                             "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]")
btnsgn.click()
emailname = driver.find_element(By.ID, "signinEmail")
emailname.send_keys("shvetsova4.cristulia@gmail.com")
passwordname = driver.find_element(By.ID, "signinPassword")
passwordname.send_keys("Isss11123")
btnlgn = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[2]")
btnlgn.click()
time.sleep(5)
'''

#реєстрація нового користувача:
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
driver.maximize_window()
kbtnsignup = driver.find_element(By.CLASS_NAME, "hero-descriptor_btn")
kbtnsignup.click()
kname = driver.find_element(By.XPATH, '//*[@id="signupName"]')
kname.send_keys("Krystyna")
klname = driver.find_element(By.ID, "signupLastName")
klname.send_keys("Udod")
kemail = driver.find_element(By.ID, "signupEmail")
kemail.send_keys("shvetsova5.cristulia@gmail.com")
kpassword = driver.find_element(By.ID, "signupPassword")
kpassword.send_keys("Isss11123")
kpassword2 = driver.find_element(By.ID, "signupRepeatPassword")
kpassword2.send_keys("Isss11123")
kregister = driver.find_element(By.CSS_SELECTOR, "body > ngb-modal-window > div > div > app-signup-modal > div.modal-footer > button")
kregister.click()
time.sleep(5)
assert "User already exists" in driver.page_source
driver.close()
'''

# додавання авто:
kbtnadd = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
kbtnadd.click()
time.sleep(5)
kautoname = driver.find_element(By.ID, "addCarBrand")
kautoname.click()
from selenium.webdriver.support.ui import Select

selectbrand = Select(driver.find_element(By.ID, "addCarBrand"))
selectbrand.select_by_value("1: 2")
kmodel = driver.find_element(By.ID, "addCarModel")
kmodel.click()
selectmodel = Select(driver.find_element(By.ID, "addCarModel"))
selectmodel.select_by_value("5: 6")
kmile = driver.find_element(By.ID, "addCarMileage")
kmile.click()
kmileage = driver.find_element(By.XPATH,
                               "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[2]/app-add-car-form/form/div[3]/div/input")
kmileage.send_keys("350")
kbtnadd2 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]")
kbtnadd2.click()
time.sleep(5)

# додавання витрат1:
kaddanexpence = driver.find_element(By.XPATH,
                                    "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]")
kaddanexpence.click()
kmileage = driver.find_element(By.XPATH,
                               "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[3]/div[1]/input")
kmileage.clear()
kmileage.send_keys("500")
knumber = driver.find_element(By.XPATH,
                              "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[4]/div[1]/input")
knumber.send_keys("20")
kcoast = driver.find_element(By.XPATH,
                             "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[5]/div[1]/input")
kcoast.send_keys("30")
kbtnadd3 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
kbtnadd3.click()
time.sleep(5)

# додавання витрат2:
kaddanexpence = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[1]/div/button")
kaddanexpence.click()
kmileage2 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[3]/div[1]/input")
time.sleep(3)
kmileage2.clear()
kmileage2.send_keys("1000")
knumber = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[4]/div[1]/input")
knumber.send_keys("50")
kcoast = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[5]/div[1]/input")
kcoast.send_keys("80")
kbtnadd4 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
kbtnadd4.click()
time.sleep(5)

# видалення користувача:
driver.get("https://qauto2.forstudy.space/panel/settings")
kremove = driver.find_element(By.XPATH,
                              "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[5]/div/button")
kremove.click()
time.sleep(2)
kremove2 = driver.find_element(By.XPATH,
                               "/html/body/ngb-modal-window/div/div/app-remove-account-modal/div[3]/button[2]")
kremove2.click()
time.sleep(3)
driver.close()
'''