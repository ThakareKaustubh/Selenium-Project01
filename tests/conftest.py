from webbrowser import Chrome
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--disable-gpu")  # Fixes issues in some systems
    chrome_options.add_argument("--window-size=1920x1080")  # Ensure elements are visible
    chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security (useful in Docker)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
    chrome_options.add_argument("--start-maximized")  # Start maximized

    # Initialize WebDriver with headless options
    driver = webdriver.Chrome(chrome_options)  # Or use Edge, Firefox, etc.
    driver.implicitly_wait(5)
    yield driver  # Provide the driver instance to tests
    driver.quit()


