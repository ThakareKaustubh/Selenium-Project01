import time
from threading import Thread
import  pytest
from selenium.webdriver.common.by import By
from base_pages.registration_page import RegistrationPage
from base_pages.login_page import LoginPage


@pytest.mark.order(1)

def test_user_registration(setup):
    driver = setup
    driver.get("https://www.automationexercise.com/login")
    time.sleep(2)
    registration_page = RegistrationPage(driver)
    time.sleep(2)

    if registration_page.verify_page_load("New User Signup!"):
        registration_page.register_username("testNamer")
        registration_page.register_email("testemail223@gmail.com")
        time.sleep(1)
        registration_page.submit_registration()
        time.sleep(1)
        registration_page.select_title()
        time.sleep(2)
        registration_page.verify_name("testNamer")
        time.sleep(1)
        registration_page.verify_email("testemail223@gmail.com")
        time.sleep(1)
        registration_page.enter_pass("TestPass@123")
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)
        registration_page.select_checkboxes()
        time.sleep(1)
        registration_page.select_bdate("4", "4", "2000" )
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 500);")
        registration_page.enter_address_details( "Kaustu", "thalaj", "company", "address1", "address2", "Singapore", "state_name", "city_name","411001", "9986734557")
        driver.execute_script("window.scrollBy(0, 500);")
        registration_page.submit_form()
        time.sleep(2)
        if registration_page.verify_account_created("Account Created!"):
            assert True

@pytest.mark.order(2)
def test_user_exists(setup):
    driver = setup
    driver.get("https://www.automationexercise.com/login")
    time.sleep(2)
    registration_page = RegistrationPage(driver)
    if registration_page.verify_page_load("New User Signup!"):
        registration_page.register_username("testNamer")
        time.sleep(1)
        registration_page.register_email("testemail223@gmail.com")
        time.sleep(1)
        registration_page.submit_registration()
        time.sleep(2)
        already_exists = driver.find_element(By.XPATH, "//p[contains(text(), 'Email Address already exist!')]")
        time.sleep(1)
        if already_exists.text == 'Email Address already exist!':
            assert True

@pytest.mark.order(3)
def test_login_existing_user(setup):
    driver = setup
    driver.get("https://www.automationexercise.com/login")
    time.sleep(2)
    login_page = LoginPage(driver)
    time.sleep(2)
    verify_page_load = driver.find_element(By.XPATH, "//h2[contains(text(), 'Login to your account')]")
    if verify_page_load.text == "Login to your account":
        login_page.enter_username("testemail223@gmail.com")
        login_page.enter_password("TestPass@123")
        time.sleep(1)
        login_page.submit_login()
        time.sleep(2)
        verify_login = driver.find_element(By.XPATH, "//h2[contains(text(), 'Full-Fledged practice website')]")
        time.sleep(1)
        if verify_login.text == 'Full-Fledged practice website':
            assert True

@pytest.mark.order(4)
def test_delete_account(setup):
    driver = setup
    driver.get("https://www.automationexercise.com/login")
    login_page = LoginPage(driver)
    time.sleep(1)
    verify_page_load = driver.find_element(By.XPATH, "//h2[contains(text(), 'Login to your account')]")
    if verify_page_load.text == "Login to your account":
        login_page.enter_username("testemail223@gmail.com")
        time.sleep(1)
        login_page.enter_password("TestPass@123")
        time.sleep(1)
        login_page.submit_login()
        time.sleep(1)
        click_del = driver.find_element(By.XPATH, "//a[contains(text(), 'Delete Account')]")
        click_del.click()
        time.sleep(1)
        verify_complete = driver.find_element(By.XPATH, "//b[contains(text(), 'Account Deleted')]")
        if verify_complete.text == "Account Deleted!":
            assert True
