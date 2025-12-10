import time
from utils.driver_setup import get_driver
from pages.search_page import SearchPage

def test_google_search():
    driver = get_driver()
    driver.get("https://www.google.com")

    search = SearchPage(driver)
    search.search("Python automation testing")

    time.sleep(2)
    assert "python" in driver.title.lower()

    driver.quit()
