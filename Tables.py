from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://practice.expandtesting.com/tables")
driver.maximize_window()
sleep(3)
element = driver.find_element(By.XPATH, ' //*[@id="table1"]/tbody/tr[4]/td[6]/a[1]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element.click()

url = driver.current_url
print(url)

driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#Open%20New%20Tab")
sleep(3)
driver.find_element(By.ID, 'iFrame').click()
sleep(3)
iframes = driver.find_elements(By.TAG_NAME, 'iframe')
iframe_count = len(iframes)
print(iframe_count)
driver.switch_to.frame("globalSqa")
sleep(3)

element = driver.find_element(By.XPATH, '//div[@class="info_desc"]/h3[text()="JMeter Training"]')
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element.click()

sleep(3)
print("clicked on it")
Expected_title = "JMeter Training"
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="page_heading"]/h1[text()="JMeter Training"]'))
)
Actual_title = driver.find_element(By.XPATH,'//div[@class="page_heading"]/h1').text
assert Actual_title == Expected_title, "Title mismatch"


sleep(3)
