from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.linkedin.com")
print(driver.title)
name = driver.find_element_by_name("session_key")
name.clear()
name.send_keys("ismail@gmail.com")
name.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
   