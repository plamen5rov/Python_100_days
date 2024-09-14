from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Deprecated - no longer needed
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_number = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')

articles_number.click()

# print(articles_number.text)