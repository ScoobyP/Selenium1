from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
try:
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    search = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
    search.send_keys('Internet Speed test')
    search.send_keys(Keys.ENTER)

    time.sleep(3)

    fastwebsite_link = driver.find_element(by=By.XPATH,
                                           value='//*[@id="rso"]/div[2]/div[2]/div/div/div/div[1]/div/div/span/a')
    fastwebsite_link.click()

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="test-context-container"]/div[1]')))

    show_more_info = driver.find_element(By.XPATH, '//*[@id="test-context-container"]').is_displayed()
    if show_more_info:
        smi_button = driver.find_element(by=By.XPATH, value='//*[@id="show-more-details-link"]')
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="show-more-details-link"]')))
        smi_button.click()
    else:
        print('No Info To Show')

    WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.ID, 'speed-value')))
    download_speed_value = driver.find_element(By.XPATH, '//*[@id="speed-value"]')
    print(f'Download Speed: {download_speed_value.text} Mbps')

    time.sleep(15)

    upload_speed_value = driver.find_element(By.XPATH, '//*[@id="upload-value"]')
    print(f'Upload Speed: {upload_speed_value.text} Mbps')

    server_loc_value = driver.find_element(By.XPATH, '//*[@id="server-locations"]')
    print(f'Server Location: {server_loc_value.text}')

    device_loc_value = driver.find_element(By.XPATH, '//*[@id="user-location"]')
    print(f'Device Location: {device_loc_value.text}')

finally:
    driver.quit()


