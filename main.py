from selenium import webdriver
import time

# Set the path to chromedriver
path_to_chromedriver = 'res/chromedriver/chromedriver.exe'

# Create the browser with the given driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

# Set the url and open it
# TODO - create login
# url = input("Introduce the URL: ");
url = 'https://www.nexis.com/auth/checkbrowser.do;jsessionid=D64BDD0264606709F496D1A201DD856A.04wtwLiVnPdMdvSvpMQaQ?t=1487707714744&bhcp=1'
browser.get(url)

time.sleep(5)

# Input search terms
browser.find_element_by_name('searchTerms1').clear()
browser.find_element_by_name('searchTerms1').send_keys('balloon')

time.sleep(5)

# Anywhere in the text
browser.find_element_by_xpath('//*[@id="simpleSrchSel"]/option[1]').click()

time.sleep(5)

# Custom date
browser.find_element_by_xpath('//*[@id="specifyDateDefaultStyle"]/option[12]').click()

time.sleep(5)

# Set custom date (the input will be the starting year

# time.sleep(10)

# browser.quit()