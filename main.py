from selenium import webdriver
import getpass
import time

# Set the path to chromedriver
path_to_chromedriver = 'res/chromedriver/chromedriver.exe'

# Create the browser with the given driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

# Set the url and open it
url = 'http://uob-metalib.hosted.exlibrisgroup.com/V/?func=native-link&resource=BHM02155'
browser.get(url)

time.sleep(10)

# Store user and password
user = input('Please provide your uob id: ')
print(user)
pwd = getpass.getpass('Please provide your uob password: ')
print(pwd)

# Complete the user field
browser.find_element_by_id('j_username').clear()
browser.find_element_by_id('j_username').send_keys(user)

time.sleep(4)

# Complete the password field
browser.find_element_by_id('j_password').clear()
browser.find_element_by_id('j_password').send_keys(pwd)

time.sleep(4)

browser.find_element_by_id('j_submit').click()

time.sleep(10)

# Input search terms
browser.find_element_by_name('searchTerms1').clear()
browser.find_element_by_name('searchTerms1').send_keys('balloon')

time.sleep(10)

# Anywhere in the text
browser.find_element_by_xpath('//*[@id="simpleSrchSel"]/option[1]').click()

time.sleep(5)

# Custom date
browser.find_element_by_xpath('//*[@id="specifyDateDefaultStyle"]/option[12]').click()

time.sleep(5)

# Set custom date (the input will be the starting year)
print("Now choose the starting date: ")
fromDateMonth = input("Input the month (mm format): ")
fromDateDay = input("Input the day (dd format): ")
fromDateYear = input("Input the year (yyyy format): ")

browser.find_element_by_id('fromDate').clear()
browser.find_element_by_id('fromDate').send_keys(fromDateMonth + '/' + fromDateDay + '/' + fromDateYear)

print("Now choose the end date: ")
toDateMonth = input("Input the month (mm format): ")
toDateDay = input("Input the day (dd format): ")
toDateYear = input("Input the year (yyyy format): ")

browser.find_element_by_id('toDate').clear()
browser.find_element_by_id('toDate').send_keys(toDateMonth + '/' + toDateDay + '/' + toDateYear)

time.sleep(2)

browser.find_element_by_xpath('//*[@id="sourceSelectDDStyle"]/option[4]').click()

time.sleep(2)

if browser.find_element_by_id('groupDuplicates').is_selected() != True:
    browser.find_element_by_id('groupDuplicates').click()

time.sleep(1)

if browser.find_element_by_id('includeWireChkBoxStyle').is_selected() == True:
    browser.find_element_by_id('includeWireChkBoxStyle').click()

time.sleep(1)

if browser.find_element_by_id('includeObituariesChkBoxStyle').is_selected() != True:
    browser.find_element_by_id('includeObituariesChkBoxStyle').click()

time.sleep(1)

if browser.find_element_by_id('includeWebsitesChkBoxStyle').is_selected() != True:
    browser.find_element_by_id('includeWebsitesChkBoxStyle').click()

time.sleep(1)

if browser.find_element_by_id('includeShortDocsChkBoxStyle').is_selected() == True:
    browser.find_element_by_id('includeShortDocsChkBoxStyle').click()

time.sleep(1)

browser.find_element_by_id('enableSearchImg').click()

time.sleep(10)

# time.sleep(10)

# browser.quit()