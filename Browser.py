from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# import keyboard
import time
from selenium.webdriver.support import expected_conditions as EC

# para actualizar el driver automaticamente
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def expand_shadow_element(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

def get_browsing_history(driver):
    """Find the "Browsing History" option on the advanced tab"""
    checkbox = driver.find_element(By.ID, value='browsingCheckbox')
    root1 = expand_shadow_element(checkbox).find_element(By.ID, value='outerRow')
    # esperamos hasta que aparezca un elemento con este id, este pertenece a 'Browsing History'
    wait = WebDriverWait(root1, 10).until(
        EC.presence_of_element_located((By.ID, "label"))
        )
    return  wait

def clearChromeCache(driver):
    
    driver.get('chrome://settings/clearBrowserData')
    root1 = driver.find_element(By.TAG_NAME, value='settings-ui')
    shadow_root1 = expand_shadow_element(root1)
    
    container = shadow_root1.find_element(By.ID, value='container')
    root2 = container.find_element(By.ID, value='main')
    shadow_root2 = expand_shadow_element(root2)
    
    root3 = shadow_root2.find_element(By.TAG_NAME, value='settings-basic-page')
    shadow_root3 = expand_shadow_element(root3)
    
    root4 = shadow_root3.find_element(By.TAG_NAME, value='settings-privacy-page')
    shadow_root4 = expand_shadow_element(root4)
    
    root5 = shadow_root4.find_element(By.TAG_NAME, value='settings-clear-browsing-data-dialog')
    shadow_root5 = expand_shadow_element(root5)
    
    # cleaing basic cache
    clear_data = shadow_root5.find_element(By.ID, value='clearBrowsingDataConfirm')
    clear_data.click()
    time.sleep(4)
    
    # click in 'clear browsing data' to delete advanced cache history
    clearBrowsingDiaglo = shadow_root4.find_element(By.ID, value='clearBrowsingData')
    clearBrowsingDiaglo.click()
    
    # finding the 'advanced tab'
    root4 = shadow_root3.find_element(By.TAG_NAME, value='settings-privacy-page')
    shadow_root4 = expand_shadow_element(root4)
    
    root5 = shadow_root4.find_element(By.TAG_NAME, value='settings-clear-browsing-data-dialog')
    shadow_root5 = expand_shadow_element(root5)
            
    root6 = shadow_root5.find_element(By.ID, value='clearBrowsingDataDialog')
    tabs = root6.find_element(By.CSS_SELECTOR, value='cr-tabs')
    shadow_root6 = expand_shadow_element(tabs)
    
    advanced_tab = shadow_root6.find_elements(By.CSS_SELECTOR, value='div')[3]
    advanced_tab.click()
    # esperemos hasta que aparezca browsing history en advanced_tab
    get_browsing_history(root6)
    # cleaing advanced cache
    clear_data = shadow_root5.find_element(By.ID, value='clearBrowsingDataConfirm')
    clear_data.click()

    driver.close()

    
if '__name__' == '__main__':
    clearChromeCache(driver)

