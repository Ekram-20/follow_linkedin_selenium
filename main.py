

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



# linkedin account
email = ''
password = '' 


# first download  webdriver from https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('/Users/ekram/Downloads/chromedriver_mac_arm64/chromedriver')

try: 
    
    # sign in page of linkedin
    driver.get('https://www.linkedin.com/')
    
    # sign in 
    driver.find_element(By.ID, 'session_key').send_keys(email)
    driver.find_element(By.ID, 'session_password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 
                        '#main-content > section.section.min-h-\[560px\].flex-nowrap.pt-\[40px\].babybear\:flex-col.babybear\:min-h-\[0\].babybear\:px-mobile-container-padding.babybear\:pt-\[24px\] > div > div > form:nth-child(7) > div.flex.justify-between.sign-in-form__footer--full-width > button').click()
            
    # got to page of Eng.Ibrahem            
    driver.get('https://www.linkedin.com/in/ibrahem-elnawasany/')
    
    # follow button
    driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button').click()

    # connect
    #driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[4]/section/div[2]/button').click()
    
    # confirm connection
    #driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
    

except Exception as e: 
    print(e)
    driver.quit()



