from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@name='name']")
        self.email_input = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signup_btn = (By.XPATH, "//input[@data-qa='signup-button']")
        self.login_email = (By.XPATH, "//input[@data-qa='login-email']")
        self.login_pass = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_btn = (By.XPATH, "//button[@data-qa='login-button']")
        self.submit_reg = (By.XPATH,"//button[@data-qa = 'signup-button']")


    def enter_username(self, login_mail):
        username_field = self.driver.find_element(*self.login_email)
        username_field.clear()  # Clear existing input
        username_field.send_keys(login_mail)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.login_pass)
        password_field.clear()
        password_field.send_keys(password)

    def register_username(self, username):
        name_field = self.driver.find_element(*self.username_input)
        name_field.clear()  # Clear existing input
        name_field.send_keys(username)

    def register_email(self, email):
        email_field = self.driver.find_element(*self.email_input)
        email_field.clear()  # Clear existing input
        email_field.send_keys(email)

    def submit_registration(self):
        self.driver.find_element(*self.submit_reg).click()

    def submit_login(self):
        self.driver.find_element(*self.login_btn).click()