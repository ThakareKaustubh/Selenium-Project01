import time

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from base_pages.login_page import LoginPage

class RegistrationPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.radio_id1 = (By.ID,"id_gender1")
        self.radio_id2 = (By.ID, "id_gender2")
        self.reg_name = (By.XPATH, "//*[@id='name']")
        self.reg_email = (By.XPATH, "//*[@id='email']")
        self.reg_pass = (By.XPATH, "//*[@id='password']")
        self.days = (By.XPATH, "//*[@id='days']")
        self.months = (By.XPATH, "//*[@id='months']")
        self.years = (By.XPATH, "//*[@id='years']")
        self.chk_box1 = (By.XPATH, "//*[@id='newsletter']")
        self.chk_box2 = (By.XPATH, "//*[@id='optin']")
        self.first_name = (By.XPATH, "//*[@id='first_name']")
        self.last_name = (By.XPATH, "//*[@id='last_name']")
        self.company = (By.XPATH, "//*[@id='company']")
        self.address1 = (By.XPATH, "//*[@id='address1']")
        self.address2 = (By.XPATH, "//*[@id='address2']")
        self.country = (By.XPATH, "//*[@id='country']")
        self.state = (By.XPATH, "//*[@id='state']")
        self.city = (By.XPATH, "//*[@id='city']")
        self.zip_code = (By.XPATH, "//*[@id='zipcode']")
        self.mobile_num = (By.XPATH, "//*[@id='mobile_number']")
        self.submit = (By.XPATH, "//button[@data-qa='create-account']")
        self.verify_page_load = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
        self.verify_complete = (By.XPATH, "//b[text()='Account Created!']")


    def select_title(self):
        radio_title1 = self.driver.find_element(*self.radio_id1)
        radio_title1.click()


    def verify_name(self,name):
        name_verify = self.driver.find_element(*self.reg_name)
        val =  name_verify.get_attribute("value")
        if val == name:
            return True
        else:
            return False

    def verify_email(self,email):
        mail_verify = self.driver.find_element(*self.reg_email)
        val = mail_verify.get_attribute("value")
        if val == email:
            return True
        else:
            return False

    def enter_pass(self,password):
        pass_field = self.driver.find_element(*self.reg_pass)
        pass_field.send_keys(password)

    def select_bdate(self, day, month, year):
        day_dropdown = self.driver.find_element(*self.days)
        month_dropdown = self.driver.find_element(*self.months)
        year_dropdown = self.driver.find_element(*self.years)

        Select(day_dropdown).select_by_value(day)

        Select(month_dropdown).select_by_value(month)

        Select(year_dropdown).select_by_value(year)

    def select_checkboxes(self):

        cb1 = self.driver.find_element(*self.chk_box1)
        cb2 = self.driver.find_element(*self.chk_box2)
        cb1.click()
        cb2.click()

    def enter_address_details(self, fname, lname, company, address1, address2, country_name, state_name, city_name,zip, mob_number):
        firstname = self.driver.find_element(*self.first_name)
        lastname = self.driver.find_element(*self.last_name)
        companyname = self.driver.find_element(*self.company)
        address_details1 = self.driver.find_element(*self.address1)
        address_details2 = self.driver.find_element(*self.address2)
        country_details = self.driver.find_element(*self.country)
        state_details = self.driver.find_element(*self.state)
        city_details = self.driver.find_element(*self.city)
        zipcode = self.driver.find_element(*self.zip_code)
        mob_num = self.driver.find_element(*self.mobile_num)

        time.sleep(2)
        firstname.send_keys(fname)
        lastname.send_keys(lname)
        companyname.send_keys(company)
        address_details1.send_keys(address1)
        address_details2.send_keys(address2)
        Select(country_details).select_by_value(country_name)
        state_details.send_keys(state_name)
        city_details.send_keys(city_name)
        zipcode.send_keys(zip)
        mob_num.send_keys(mob_number)

    def submit_form(self):
        self.driver.find_element(*self.submit).click()

    def verify_page_load(self, verify_text):
        if self.driver.find_element(*self.verify_page_load).text == verify_text:
            return True

    def verify_account_created(self, acc_complete):
        if self.driver.find_element(*self.verify_complete).text == acc_complete:
            return True


