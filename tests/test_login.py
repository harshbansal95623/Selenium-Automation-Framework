import time
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

def test_login_success():
    driver = get_driver()
    driver.get("https://example.com/login")

    login = LoginPage(driver)
    login.enter_username("test_user")
    login.enter_password("password123")
    login.click_login()

    time.sleep(2)
    assert "dashboard" in driver.current_url.lower()

    driver.quit()
