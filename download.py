import time
import pyautogui
import pygetwindow as gw
from pywinauto import Application
from pywinauto.keyboard import SendKeys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome driver
chrome_service = ChromeService(executable_path='chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to login page
driver.get('https://reader-prod.gls.pearson-intl.com/products/171882/pages/488?locale=&userPreferredType=read&iesCode=V13zIZKEVn')


# Wait for the login page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

# Enter username and password
driver.find_element(By.NAME, 'username').send_keys('ADD USERNAME')
driver.find_element(By.NAME, 'password').send_keys('ADD PASSWORD')
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

#wait for 10 seconds
time.sleep(10)

# Download pages
for page_num in range(441, 472):
    # Navigate to page
    driver.get(f'https://etext-content.gls.pearson-intl.com/eplayer/pdfassets/prod1/171882/bc2496e9-e409-4117-bda7-8e0c929f5220/pages/page{page_num}?password=&accessToken=null&formMode=true')

    # Wait for page to load
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas#pdf-canvas')))

    # Scroll to bottom to load full page
    #canvas = driver.find_element(By.CSS_SELECTOR, 'canvas#pdf-canvas')
    #driver.execute_script('arguments[0].scrollIntoView(false);', canvas)
    time.sleep(10)

    # Save screenshot
    #driver.save_screenshot(f'page{page_num}.png')

# Close the browser
driver.quit()
