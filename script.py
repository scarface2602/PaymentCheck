import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# get the path of ChromeDriverServer
chrome_driver_path = "/Users/Sudeep/Downloads/chromedriver"
# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)

URL = 'https://payments.tripfactory.com/payments/payment-moto?cnf=TFN000TBO8M&pid=62183'
CSS_SELECTOR = 'li.curPoint.payTbNET_BANKING'
bank=["//select[@name='issuerCode']/option[@value='STATE_BANK_OF_TRAVANCORE']","//select[@name='issuerCode']/option[@value='INDUSIND_BANK']","//select[@name='issuerCode']/option[@value='SOUTH_INDIAN_BANK']","//select[@name='issuerCode']/option[@value='DENA_BANK']","//select[@name='issuerCode']/option[@value='PUNJAB_NATIONAL_BANK_RETAIL_ACCOUNTS']","//select[@name='issuerCode']/option[@value='UNION_BANK']","//select[@name='issuerCode']/option[@value='KARNATAKA_BANK']","//select[@name='issuerCode']/option[@value='CATHOLIC_SYRIAN_BANK']","//select[@name='issuerCode']/option[@value='HDFC_BANK']","//select[@name='issuerCode']/option[@value='INDIAN_BANK']","//select[@name='issuerCode']/option[@value='IDBI_BANK']","//select[@name='issuerCode']/option[@value='UNION_BANK_CORPORATE']","//select[@name='issuerCode']/option[@value='SBI_BANK']","//select[@name='issuerCode']/option[@value='BANK_OF_BARODA']","//select[@name='issuerCode']/option[@value='LAKSHMI_VILAS_BANK_NETBANKING']","//select[@name='issuerCode']/option[@value='BANK_OF_MAHARASHTRA']","//select[@name='issuerCode']/option[@value='SARASWAT_BANK']","//select[@name='issuerCode']/option[@value='DEUTSCHE_BANK']","//select[@name='issuerCode']/option[@value='CORPORATION_BANK']","//select[@name='issuerCode']/option[@value='FEDERAL_BANK']","//select[@name='issuerCode']/option[@value='STANDARD_CHARTERED_BANK']","//select[@name='issuerCode']/option[@value='STATE_BANK_OF_MYSORE']","//select[@name='issuerCode']/option[@value='DCB_BANK__DEVELOPMENT_CREDIT_BANK_CORPORATE']","//select[@name='issuerCode']/option[@value='ING_VYSYA_BANK']"
,"//select[@name='issuerCode']/option[@value='PUNJAB_NATIONAL_BANK_CORPORATE_ACCOUNTS']","//select[@name='issuerCode']/option[@value='BANK_OF_BARODA_CORPORATE_ACCOUNTS']","//select[@name='issuerCode']/option[@value='VIJAYA_BANK']","//select[@name='issuerCode']/option[@value='STATE_BANK_OF_BIKANER_AND_JAIPUR']","//select[@name='issuerCode']/option[@value='INDUSTRIAL_DEVELOPMENT_BANK_OF_INDIA']","//select[@name='issuerCode']/option[@value='BANK_OF_BARODA_RETAIL_ACCOUNTS']","//select[@name='issuerCode']/option[@value='ICICI_BANK']","//select[@name='issuerCode']/option[@value='STATE_BANK_OF_HYDERABAD']","//select[@name='issuerCode']/option[@value='ALLAHABAD_BANK']","//select[@name='issuerCode']/option[@value='ORIENTAL_BANK_OF_COMMERCE']","//select[@name='issuerCode']/option[@value='INDIAN_OVERSEAS_BANK']","//select[@name='issuerCode']/option[@value='CENTRAL_BANK_OF_INDIA']","//select[@name='issuerCode']/option[@value='ANDHRA_BANK']","//select[@name='issuerCode']/option[@value='SHAMRAO_VITTHAL_CO_OP_BANK']","//select[@name='issuerCode']/option[@value='RATNAKAR_BANK']","//select[@name='issuerCode']/option[@value='YES_BANK']","//select[@name='issuerCode']/option[@value='UNITED_BANK_OF_INDIA']","//select[@name='issuerCode']/option[@value='KOTAK_MAHINDRA_BANK']","//select[@name='issuerCode']/option[@value='STATE_BANK_OF_PATIALA']","//select[@name='issuerCode']/option[@value='BANK_OF_BAHRAIN__KUWAIT']","//select[@name='issuerCode']/option[@value='CITIBANK']","//select[@name='issuerCode']/option[@value='CANARA_BANK']","//select[@name='issuerCode']/option[@value='JAMMU__KASHMIR_BANK']","//select[@name='issuerCode']/option[@value='KARURVYSYA_BANK']","//select[@name='issuerCode']/option[@value='BANK_OF_INDIA']"
,"//select[@name='issuerCode']/option[@value='CITY_UNION_BANK']","//select[@name='issuerCode']/option[@value='LAKSHMI_VILAS_BANK_CORPORATE_NETBANKING']","//select[@name='issuerCode']/option[@value='AXIS_BANK']","//select[@name='issuerCode']/option[@value='DCB_BANK__DEVELOPMENT_CREDIT_BANK']"]


def iterate(bname):
# navigate to the application home page
    driver.get(URL)
    driver.implicitly_wait(1) # seconds

# select payment method
    close = driver.find_element_by_css_selector(CSS_SELECTOR)
    close.click()

#select bank name
    select_bank = driver.find_element_by_xpath(bname).click()

#check terms and condition checkbox
    driver.find_element_by_xpath(".//div[@class='nb-post-selection-show']/input[@id='read_terms']").click()
#click Pay Now button
    driver.find_element_by_xpath(".//div[@class='f-item nb-post-selection-show']/a[@class='search-button']").click()
    driver.implicitly_wait(10) # seconds
#bank_name=driver.find_element_by_xpath(".//img[@class='cm-axisLogo']")
    curUrl = driver.current_url
    print (curUrl)

#with open("Netbanking.csv", "w") as file:
for name in bank:
    iterate(name)
