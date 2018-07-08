#Python Script

from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('headless')

#set the window size
options.add_argument('window-size=1200x600')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

#vist our website
driver.get('https://bearfounders.com/login')

# wait up to 10 seconds for the elements to become available
driver.implicitly_wait(10)

driver.get_screenshot_as_file('login.png')

#find the forms we want to fill in through CSS selectors
email = driver.find_element_by_css_selector('input[type=text]')
password = driver.find_element_by_css_selector('input[type=password]')
login = driver.find_element_by_css_selector('input[value="Login"]')

#fill in the forms
email.send_keys('tinazhao@berkeley.edu')
password.send_keys('mypasswordsucks')

#check that it works
driver.get_screenshot_as_file('login-page.png')

login.click()
#driver.implicitly_wait(5)
driver.get_screenshot_as_file('main-page.png')

jobs = driver.find_element_by_css_selector('a[data-category=jobs]')
jobs.click()
driver.implicitly_wait(10)
driver.get_screenshot_as_file('jobs-page.png')

#dropdowns = driver.find_elements_by_class_name('current')
#dropdowns = driver.find_elements_by_css_selector('.nice-select.filter.small')
#dropdowns = driver.find_elements_by_css_selector('.selects.jobs.is-visible')
dropdowns = driver.find_elements_by_class_name('filter-container')
#dropdowns = driver.find_elements_by_class_name('nice-select filter small')
print(len(dropdowns))
for i in range(0, len(dropdowns)):
	print(dropdowns[i].is_displayed())
dropdown = dropdowns[6]
dropdown.click()

driver.get_screenshot_as_file('dropdown.png')

technology = driver.find_element_by_css_selector('li[data-value=TECH]')
technology.click()

driver.get_screenshot_as_file('dropdown-click.png')

go = driver.find_element_by_class_name('cd-search-button')
go.click()

driver.get_screenshot_as_file('after-go.png')



