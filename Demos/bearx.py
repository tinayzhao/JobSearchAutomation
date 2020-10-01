#Selenium Script
#refer to https://hackmd.io/s/rkBppauWm for a walkthrough

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

#fill in the forms with username and password
email.send_keys(secret.username)
password.send_keys(secret.password)

#check that it works
driver.get_screenshot_as_file('login-page.png')

#find the login button and click it
login = driver.find_element_by_css_selector('input[value="Login"]')
login.click()


driver.implicitly_wait(1000)
driver.get_screenshot_as_file('post_login.png')


dropdowns = driver.find_element_by_id('navbarDropdown')
dropdowns.click();

driver.get_screenshot_as_file('dropdown.png')

jobs = driver.find_element_by_link_text('Jobs')
jobs.click()

driver.get_screenshot_as_file('dropdown-click.png')


position_elements = driver.find_elements_by_tag_name('h6');
position_names = []
for elem in position_elements:
  position_names.append(elem.text)

#check text in elements of positions
#for elem in positions:
  #print(elem.text)

all_links = driver.find_elements_by_xpath("//a[@href]")

# check links in elements of all_links
#for elem in all_links:
  #print(elem.get_attribute("href"))


#hardcoding to obtain the relevant links
wanted_links = all_links[13:33]
application_links = []
add_link = 1
for elem in wanted_links:
  if add_link == 1:
    application_links.append(elem.get_attribute("href"))
    add_link = 0
  else:
    add_link = 1

#check application_links
#print(application_links)

table_list = [position_names, application_links]

print(table_list)
