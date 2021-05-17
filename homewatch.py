print('>initializing...')
from selenium import webdriver
from threading import Event
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Set to not show the gui
opts = webdriver.FirefoxOptions()
# opts.headless = True

# Initialize the webdriver
driver = webdriver.Firefox(options=opts, executable_path="/home/stm/.drivers/geckodriver")
driver.implicitly_wait(3)
print('>site loading...')

# Load the website
driver.get('http://192.168.254.254/html/overview.html')
print('>site loaded...')

# Click the login
js = 'loginout();'
driver.execute_script(js)
print('>executed the loginout() function...')

# Add the username and password
Event().wait(1) # Wait for 1 second before executing the adding
driver.find_element_by_xpath('//*[@id="username"]').send_keys("user")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("@l03e1t3")
print('>user and password entered...')

# Execute the login function
login = 'login("home.html");'
driver.execute_script(login)
print('>logged in...')

# Click the SMS button
print('>waiting for 3 seconds...')
time.sleep(4) # Wait 3 seconds before executing the functions below
sms = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="menu_sms"]'))
)
sms.click()
# Open the new message dialog
newmsg = 'sms_newMessage();'
driver.execute_script(newmsg)
print('>opened the new message dialog...')

# Enter the 8080 and DATABAL
time.sleep(3) # Wait for 3 seconds before executing the commands
driver.find_element_by_xpath('//*[@id="recipients_number"]').send_keys("8080")
driver.find_element_by_xpath('//*[@id="message_content"]').send_keys("HOMEWATCH199")
print('>writing the message...')

# Click the send button
send = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="pop_send"]'))
)
send.click()
print('>clicked the send button...')

# Click the ok button after done sending
send = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="pop_OK"]'))
)
send.click()
print('>message sent...')

# Refresh the site to make sure the message was received
driver.refresh()
print('>site refreshed...')

# Print the latest text message
txt = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div[2]/div[3]/table[1]/tbody/tr[2]/td[3]/pre')
print(txt[0].text) 

# Close the driver
driver.quit()