import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

c = csv.writer(open("MYFILE.csv", "wb"))

URL = 'https://payments.tripfactory.com/payments/payment-moto?cnf=TFN000TBO8M&pid=62183'
CSS_SELECTOR = 'li.curPoint.payTbNET_BANKING'
axis_bank="//select[@name='issuerCode']/option[@value='AXIS_BANK']"

# get the path of ChromeDriverServer
#dir = os.path.dirname(__file__)
chrome_driver_path = "/Users/Sudeep/Downloads/chromedriver"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)

# navigate to the application home page
driver.get(URL)
driver.implicitly_wait(1) # seconds


# select payment method
close = driver.find_element_by_css_selector(CSS_SELECTOR)
close.click()

#select bank name
select_bank = driver.find_element_by_xpath(axis_bank).click()

#check terms and condition checkbox
driver.find_element_by_xpath(".//div[@class='nb-post-selection-show']/input[@id='read_terms']").click()
#click Pay Now button
driver.find_element_by_xpath(".//div[@class='f-item nb-post-selection-show']/a[@class='search-button']").click()
driver.implicitly_wait(5) # seconds

#bank_name=driver.find_element_by_xpath(".//img[@class='cm-axisLogo']")
print (driver.current_url)
