import pytest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    print("Init driver")
    driver = Chrome()
    yield driver
    print("Quit driver")
    driver.quit()


def test_reg_userexists(driver):
    # driver = Chrome()
    # driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # seconds
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    kbtnsignup = driver.find_element(By.CLASS_NAME, "hero-descriptor_btn")
    kbtnsignup.click()
    kname = driver.find_element(By.ID, "signupName")
    kname.send_keys("Krystyna")
    klname = driver.find_element(By.ID, "signupLastName")
    klname.send_keys("Udod")
    kemail = driver.find_element(By.ID, "signupEmail")
    kemail.send_keys("shvetsova15.cristulia@gmail.com")
    kpassword = driver.find_element(By.ID, "signupPassword")
    kpassword.send_keys("Isss11123")
    kpassword2 = driver.find_element(By.ID, "signupRepeatPassword")
    kpassword2.send_keys("Isss11123")
    register = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
    register.click()
    ktitle = driver.find_element(By.XPATH, "//*[@class='alert alert-danger']")
    assert 'User already exists' in ktitle.text
    register.click()
    driver.close()

def test_signin_success(driver):
    driver.implicitly_wait(15)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    ksignin = driver.find_element(By.XPATH, "//*[@class='btn btn-outline-white header_signin']")
    ksignin.click()
    kusername = driver.find_element(By.ID, "signinEmail")
    kusername.send_keys("shvetsova15.cristulia@gmail.com")
    kpassword = driver.find_element(By.ID, "signinPassword")
    kpassword.send_keys("Isss11123")
    klogin = driver.find_element(By.XPATH, "//*[@class ='btn btn-primary']")
    klogin.click()
    kmyprofile = driver.find_element(By.ID, "userNavDropdown")
    assert 'My profile' in kmyprofile.text
    driver.close()

def test_kaddcar(driver):
    driver.implicitly_wait(5)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    ksignin = driver.find_element(By.XPATH, "//*[@class='btn btn-outline-white header_signin']")
    ksignin.click()
    kusername = driver.find_element(By.ID, "signinEmail")
    kusername.send_keys("shvetsova15.cristulia@gmail.com")
    kpassword = driver.find_element(By.ID, "signinPassword")
    kpassword.send_keys("Isss11123")
    klogin = driver.find_element(By.XPATH, "//*[@class ='btn btn-primary']")
    klogin.click()
    wait = WebDriverWait(driver, 10)
    kadd = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button")))
    kadd.click()
    kselectbrand = Select(wait.until(EC.visibility_of_element_located((By.ID, "addCarBrand"))))
    kselectbrand.select_by_value("1: 2")
    kmodel = Select(wait.until(EC.presence_of_element_located((By.ID, "addCarModel"))))
    kmodel.select_by_value("5: 6")
    kmile = wait.until(EC.element_to_be_clickable((By.ID, "addCarMileage")))
    kmile.send_keys("350")
    kaddcar1 = driver.find_element(By.CSS_SELECTOR, "div.modal-footer.d-flex.justify-content-end>button.btn.btn-primary")
    kaddcar1.click()
    kfuel = driver.find_element(By.XPATH, "//*[@class='car_add-expense btn btn-success']")
    assert 'Add fuel expense' in kfuel.text
    driver.close()


def test_kaddanexpence(driver):
    driver.implicitly_wait(5)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    ksignin = driver.find_element(By.XPATH, "//*[@class='btn btn-outline-white header_signin']")
    ksignin.click()
    kusername = driver.find_element(By.ID, "signinEmail")
    kusername.send_keys("shvetsova15.cristulia@gmail.com")
    kpassword = driver.find_element(By.ID, "signinPassword")
    kpassword.send_keys("Isss11123")
    klogin = driver.find_element(By.XPATH, "//*[@class ='btn btn-primary']")
    klogin.click()
    wait = WebDriverWait(driver, 10)
    kaddanexpence = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]")))
    kaddanexpence.click()
    kmileage = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[3]/div[1]/input")
    kmileage.clear()
    kmileage.send_keys("500")
    knumber = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[4]/div[1]/input")
    knumber.send_keys("20")
    kcoast = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[5]/div[1]/input")
    kcoast.send_keys("30")
    kbtnadd3 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
    kbtnadd3.click()
    wait = WebDriverWait(driver, 10)
    kaddanexpence2 = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[1]/div/button")))
    kaddanexpence2.click()
    wait = WebDriverWait(driver, 10)
    kmileage2 = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[3]/div[1]/input")))
    kmileage2.clear()
    kmileage2.send_keys("1000")
    knumber = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[4]/div[1]/input")
    knumber.send_keys("50")
    kcoast = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[2]/app-add-expense-form/form/div[5]/div[1]/input")
    kcoast.send_keys("80")
    kbtnadd4 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
    kbtnadd4.click()
    driver.close()

def test_kdelete(driver):
    driver.implicitly_wait(10)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    ksignin = driver.find_element(By.XPATH, "//*[@class='btn btn-outline-white header_signin']")
    ksignin.click()
    kusername = driver.find_element(By.ID, "signinEmail")
    kusername.send_keys("shvetsova15.cristulia@gmail.com")
    kpassword = driver.find_element(By.ID, "signinPassword")
    kpassword.send_keys("Isss11123")
    klogin = driver.find_element(By.XPATH, "//*[@class ='btn btn-primary']")
    klogin.click()
    kmyprofile = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/button")
    kmyprofile.click()
    ksettings = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/nav/div[1]/a[2]")
    ksettings.click()
    kremove = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[5]/div/button")
    kremove.click()
    kremove2 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-remove-account-modal/div[3]/button[2]")
    kremove2.click()
    driver.close()
