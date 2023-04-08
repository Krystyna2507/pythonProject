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
    driver.implicitly_wait(3)  # seconds
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    signup = driver.find_element(By.CLASS_NAME, "hero-descriptor_btn")
    signup.click()
    name = driver.find_element(By.ID, "signupName")
    name.send_keys("Zhanna")
    lastname = driver.find_element(By.ID, "signupLastName")
    lastname.send_keys("Orl")
    email = driver.find_element(By.ID, "signupEmail")
    email.send_keys("jane@gmail.com")
    password = driver.find_element(By.ID, "signupPassword")
    password.send_keys("Welcomej12345")
    repassword = driver.find_element(By.ID, "signupRepeatPassword")
    repassword.send_keys("Welcomej12345")
    register = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
    register.click()
    jtitle = driver.find_element(By.XPATH, "//*[@class='alert alert-danger']")
    assert 'User already exists' in jtitle.text
    register.click()
    driver.close()

def test_signin_success(driver):
    driver.implicitly_wait(3)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    signin = driver.find_element(By.XPATH, "//*[@class='btn btn-outline-white header_signin']")
    signin.click()
    jusername = driver.find_element(By.ID, "signinEmail")
    jusername.send_keys("johnsallivan@test.com")
    jpassword = driver.find_element(By.ID, "signinPassword")
    jpassword.send_keys("Qwerty12345")
    jlogin = driver.find_element(By.XPATH, "//*[@class ='btn btn-primary']")
    jlogin.click()
    jmyprofile = driver.find_element(By.ID, "userNavDropdown")
    assert 'My profile' in jmyprofile.text
    driver.close()

def test_jaddcar(driver):
    driver.implicitly_wait(5)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    signin = driver.find_element(By.XPATH, "//*[@class='btn btn-outline-white header_signin']")
    signin.click()
    jusername = driver.find_element(By.ID, "signinEmail")
    jusername.send_keys("johnsallivan@test.com")
    jpassword = driver.find_element(By.ID, "signinPassword")
    jpassword.send_keys("Qwerty12345")
    jlogin = driver.find_element(By.XPATH, "//*[@class ='btn btn-primary']")
    jlogin.click()
    wait = WebDriverWait(driver, 10)
    jadd = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button")))
    jadd.click()
    jselectbrand = Select(wait.until(EC.visibility_of_element_located((By.ID, "addCarBrand"))))
    jselectbrand.select_by_value("0: 1")
    jmodel = Select(wait.until(EC.presence_of_element_located((By.ID, "addCarModel"))))
    jmodel.select_by_value("1: 2")
    jmile = wait.until(EC.element_to_be_clickable((By.ID, "addCarMileage")))
    jmile.send_keys("100")
    jaddcar1 = driver.find_element(By.CSS_SELECTOR, "div.modal-footer.d-flex.justify-content-end>button.btn.btn-primary")
    jaddcar1.click()
    jfuel = driver.find_element(By.XPATH, "//*[@class='car_add-expense btn btn-success']")
    assert 'Add fuel expense' in jfuel.text
    driver.close()