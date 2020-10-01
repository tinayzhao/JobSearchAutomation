#Selenium Script

from selenium import webdriver
from remotework import *
from new_db import *
from airtable_api import *
from airtable import Airtable
import time
import secret

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

#driver.get_screenshot_as_file('login.png')

#find the forms we want to fill in through CSS selectors
email = driver.find_element_by_css_selector('input[type=text]')
password = driver.find_element_by_css_selector('input[type=password]')
login = driver.find_element_by_css_selector('input[value="Login"]')

#fill in the forms
email.send_keys(secret.username)
password.send_keys(secret.password)

#check that it works
#driver.get_screenshot_as_file('login-page.png')

login.click()
#driver.implicitly_wait(5)
#driver.get_screenshot_as_file('main-page.png')

jobs = driver.find_element_by_css_selector('a[data-category=jobs]')
jobs.click()
driver.implicitly_wait(10)
#driver.get_screenshot_as_file('jobs-page.png')

dropdowns = driver.find_elements_by_class_name('filter-container')

dropdown = dropdowns[6]
dropdown.click()

#driver.get_screenshot_as_file('dropdown.png')

technology = driver.find_element_by_css_selector('li[data-value=TECH]')
technology.click()

#driver.get_screenshot_as_file('dropdown-click.png')

go = driver.find_element_by_class_name('cd-search-button')
go.click()

#driver.get_screenshot_as_file('after-go.png')


SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#driver.get_screenshot_as_file('scroll_down.png')

companies = driver.find_elements_by_tag_name('h2')

jobs = driver.find_elements_by_tag_name('h3')

all_links = driver.find_elements_by_xpath("//a[@href]")

job_links_elem = all_links[8:-3]

job_links = []
for elem in job_links_elem:
	job_links.append(elem.get_attribute("href"))


table_list = [companies, jobs, job_links, current_date(len(companies)), source("BearFounders", len(companies))]

#Populate SQLite3 tables
drop_table('Bear_founders')
create_table('Bear_founders', ['Company', 'Position', 'Link', 'UpdateDate', 'Source'], ['TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT'])
populate_table('Bear_founders', 1, table_list)


#Airtable API
populate_airtable(get_rows('Bear_founders'), get_all_columns('Bear_founders'))

#Test printing and exporting
#new_db.print_table('Bear_founders')


