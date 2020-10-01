

from selenium import webdriver
import secret

options = webdriver.ChromeOptions()

options.add_argument('headless')

#set the window size
options.add_argument('window-size=1200x600')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

#vist our website
driver.get('https://bearx.co/login/')

# wait up to 10 seconds for the elements to become available
driver.implicitly_wait(10)

driver.get_screenshot_as_file('login.png')

#find the forms we want to fill in through CSS selectors
email = driver.find_element_by_css_selector('input[type=email]')
password = driver.find_element_by_css_selector('input[type=password]')
login = driver.find_element_by_css_selector('input[value="Login"]')

#fill in the forms
email.send_keys(secret.username)
password.send_keys(secret.password)

#check that it works
driver.get_screenshot_as_file('login-page.png')