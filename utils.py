import sys
import time
import random

import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

path_to_log = 'logs/'
log_errors = open(path_to_log + 'log_errors.txt', mode='w')


def checkmonth(month):
    """Check that an input is a valid month"""

    monthinteger = int(month)
    if monthinteger < 1 or monthinteger > 12:
        print("ERROR: INVALID MONTH")
        return False
    return True

# END OF checkmonth FUNCTION

def checkyear(year):
    """Check that an input is a valid year"""

    yearinteger = int(year)
    numofdigits = 0
    while yearinteger != 0:
        yearinteger = int(yearinteger / 10)
        numofdigits += 1

    if numofdigits != 4:
        print("ERROR: INVALID YEAR")
        return False
    return True


# END OF checkyear FUNCTION

def checkday(day, month, year):
    """Check that the day is valid given the day and a valid month and year"""

    monthinteger = int(month)
    dayinteger = int(day)
    yearinteger = int(year)
    if monthinteger == 1:
        if dayinteger < 1 or dayinteger > 31:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 2:
        if yearinteger % 4 == 0:
            if dayinteger < 1 or dayinteger > 29:
                print("ERROR: INVALID DAY")
                return False
        else:
            if dayinteger < 1 or dayinteger > 28:
                print("ERROR: INVALID DAY")
                return False
    elif monthinteger == 3:
        if dayinteger < 1 or dayinteger > 31:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 4:
        if dayinteger < 1 or dayinteger > 30:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 5:
        if dayinteger < 1 or dayinteger > 31:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 6:
        if dayinteger < 1 or dayinteger > 30:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 7:
        if dayinteger < 1 or dayinteger > 31:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 8:
        if dayinteger < 1 or dayinteger > 31:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 9:
        if dayinteger < 1 or dayinteger > 30:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 10:
        if dayinteger < 1 or dayinteger > 31:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 11:
        if dayinteger < 1 or dayinteger > 30:
            print("ERROR: INVALID DAY")
            return False
    elif monthinteger == 12:
        if dayinteger < 1 or dayinteger > 31:
            print("ERROR: INVALID DAY")
            return False
    return True


# END OF checkday FUNCTION

def canvaslogin(browser, uid, pwd):
    """Canvas login through library for Nexis access"""

    wait_by_id(browser, 'j_submit', EC.element_to_be_clickable, "ERROR LOADING CANVAS PAGE: CHECK INTERNET CONNECTION?")
    # Complete the user field
    browser.find_element_by_id('j_username').clear()
    browser.find_element_by_id('j_username').send_keys(uid)

    time.sleep(2)

    # Complete the password field
    browser.find_element_by_id('j_password').clear()
    browser.find_element_by_id('j_password').send_keys(pwd)

    time.sleep(2)

    browser.find_element_by_id('j_submit').click()


# END OF canvaslogin FUNCTION

def gotonews(browser):
    """Go to the News page"""
    wait_by_xpath(browser, '//*[@id="primarytabs"]/ul/li[1]/a', EC.element_to_be_clickable,
                  "ERROR LOADING NEXIS PAGE: CHECK INTERNET CONNECTION OR MAYBE CANVAS LOGIN FAILED?")
    print("LOGGED IN WITH UOB CREDENTIALS SUCCESSFULLY")
    print("CONFIRMED ON NEXIS PAGE")
    browser.find_element_by_xpath('//*[@id="primarytabs"]/ul/li[1]/a').click()
    wait_by_xpath(browser, '//*[@id="secondarytabs"]/ul/li[3]/a', EC.element_to_be_clickable,
                  "ERROAR LOADING SEARCH PAGE: CHECK INTERNET CONNECTION?")
    print("CONFIRMED ON THE SEARCH PAGE")
    browser.find_element_by_xpath('//*[@id="secondarytabs"]/ul/li[3]/a').click()


# END OF gotobrowser FUNCTION

def searchpage(browser, searchterm, fromdate, todate):
    """Config the search page and search on the new page"""

    wait_by_id(browser, 'enableSearchImg', EC.element_to_be_clickable,
               "ERROR LOADING SEARCH NEWS PAGE: CHECK INTERNET CONNECTION?")
    print("CONFIRMED ON THE SEARCH NEWS PAGE")
    # Input search terms
    browser.find_element_by_name('searchTerms1').clear()
    browser.find_element_by_name('searchTerms1').send_keys(searchterm)

    time.sleep(10)

    # Anywhere in the text
    browser.find_element_by_xpath('//*[@id="simpleSrchSel"]/option[1]').click()

    time.sleep(5)

    # Custom date
    browser.find_element_by_xpath('//*[@id="specifyDateDefaultStyle"]/option[12]').click()

    time.sleep(5)

    # Set custom date (the input will be the starting year)

    # Set the from date to the input items
    browser.find_element_by_id('fromDate').clear()
    browser.find_element_by_id('fromDate').send_keys(fromdate)

    # Set the to date to the input items
    browser.find_element_by_id('toDate').clear()
    browser.find_element_by_id('toDate').send_keys(todate)

    time.sleep(2)

    # Check All English Texts
    browser.find_element_by_xpath('//*[@id="sourceSelectDDStyle"]/option[4]').click()

    time.sleep(2)

    # No duplicates
    if not browser.find_element_by_id('groupDuplicates').is_selected():
        browser.find_element_by_id('groupDuplicates').click()

    time.sleep(1)

    # False
    if browser.find_element_by_id('includeWireChkBoxStyle').is_selected():
        browser.find_element_by_id('includeWireChkBoxStyle').click()

    time.sleep(1)

    # True
    if not browser.find_element_by_id('includeObituariesChkBoxStyle').is_selected():
        browser.find_element_by_id('includeObituariesChkBoxStyle').click()

    time.sleep(1)

    # True
    if not browser.find_element_by_id('includeWebsitesChkBoxStyle').is_selected():
        browser.find_element_by_id('includeWebsitesChkBoxStyle').click()

    time.sleep(1)

    # False
    if browser.find_element_by_id('includeShortDocsChkBoxStyle').is_selected():
        browser.find_element_by_id('includeShortDocsChkBoxStyle').click()

    time.sleep(1)

    # Search item
    browser.find_element_by_id('enableSearchImg').click()

    time.sleep(15)
    print("Searched succesfully!")


# END OF searchpage FUNCTION

def check_no_documents(browser):
    """Check if the NoDocumentsFound page appears"""

    try:
        browser.find_element_by_xpath('//*[@id="results"]/h1')
        # TODO - start the search for another term again?!
        print("NO RESULTS FOUND")
    except NoSuchElementException:
        pass


# END OF check_no_documents FUNCTION

def check_many_results(browser):
    """Check if the 3000+ results page appears"""

    try:
        browser.find_element_by_xpath('//*[@id="popupContainer"]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/span')
        wait_by_xpath(browser, '(//*[@id="firstbtn"])[2]', EC.element_to_be_clickable,
                      "COULD NOT CLICK THE 'RETRIEVE RESULTS' BUTTON.")
        browser.find_element_by_xpath('(//*[@id="firstbtn"])[2]').click()
        print("3000+ RESULTS FOUND\nRETRIEVE RESULTS PRESSED")

    except NoSuchElementException:
        pass


# END OF check_many_results FUNCTION

def manage_download(browser):
    """Manage the download"""
    wait_by_id(browser, 'TotalCountDiv', EC.presence_of_element_located,
               "ERROR LOADING THE RESULTS PAGE: MAYBE INTERNET CONNECTION PROBLEM?")
    search_text = browser.find_element_by_id('TotalCountDiv').get_attribute('innerHTML')
    search_result_string = ''

    for i in range(2, len(search_text) - 2):
        search_result_string += search_text[i]

    search_result_count = int(search_result_string)
    print(search_result_count)

    error = False
    if search_result_count <= 500:
        initial = 1
        final = search_result_count
    else:
        initial = 1
        final = 500
    while initial <= search_result_count:
        limit = str(initial) + '-' + str(final)
        print(limit)  # TODO - CREATE LOG

        download(browser, limit, error)

        # Wait for the closeBtn to show-up: if it does not show up, check for an error
        try:
            WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.ID, 'errorAlign')))
            error_msg = str(browser.find_element_by_id('errorAlign').get_attribute('innerHTML'))
            new_error_msg = error_msg.replace('.', '')
            search_result_count = [int(i) for i in new_error_msg.split() if i.isdigit()][0]

            error = True
            print(
                "After similarity analysis, the document number count is now " +
                str(search_result_count) +
                " . One or more of the document numbers you entered fell outside that range."
            )

        except TimeoutException:
            try:
                WebDriverWait(browser, 600).until(EC.element_to_be_clickable((By.ID, 'closeBtn')))
                browser.find_element_by_id('closeBtn').click()

                error = False
            except TimeoutException:
                print("ERROR LOADING THE DOWNLOAD PAGE: MAYBE INTERNET CONNECTION PROBLEM?")
                log_errors.write("ERROR LOADING THE DOWNLOAD PAGE: MAYBE INTERNET CONNECTION PROBLEM?" + '\n')
                browser.quit()
                sys.exit(1)

        if not error:
            initial += 500
        difference = search_result_count - final
        if difference <= 500:
            final += difference
        else:
            final += 500

        wait_random_time()
        # END OF WHILE LOOP

    wait_random_time()

    browser.find_element_by_xpath('//*[@id="editsearch"]/span/a').click()

# END OF manage_download FUNCTION


def download(browser, limit, error):
    """Download the files with this configuration and the given limit (range)"""

    if not error:
        # Press download section
        browser.find_element_by_id('delivery_DnldRender').click()

        time.sleep(5)

    # Press Download Options
    browser.find_element_by_xpath('//*[@id="tabs"]/ul/li[1]/a').click()

    time.sleep(1)

    # Set "Select Items"
    if not browser.find_element_by_id('sel').is_selected():
        browser.find_element_by_id('sel').click()

    time.sleep(1)

    browser.find_element_by_id('rangetextbox').clear()
    browser.find_element_by_id('rangetextbox').send_keys(limit)

    # Press Page Options
    browser.find_element_by_xpath('//*[@id="tabs"]/ul/li[2]/a').click()

    time.sleep(1)

    # Set Cover Page true if it is not set
    if not browser.find_element_by_id('cvpg').is_selected():
        browser.find_element_by_id('cvpg').click()

    time.sleep(1)

    # Set List of included documents true if it is not set
    if not browser.find_element_by_id('inclDocs').is_selected():
        browser.find_element_by_id('inclDocs').click()

    time.sleep(1)

    # Set End Page true if it is not set
    if not browser.find_element_by_id('endpg').is_selected():
        browser.find_element_by_id('endpg').click()

    time.sleep(1)

    # Set Each Document on a new page if it is not set
    if not browser.find_element_by_id('docnewpg').is_selected():
        browser.find_element_by_id('docnewpg').click()

    time.sleep(1)

    # Press Format Options
    browser.find_element_by_xpath('//*[@id="tabs"]/ul/li[3]/a').click()

    time.sleep(1)

    # Set document format to generic
    browser.find_element_by_xpath('//*[@id="delFmt"]/option[3]').click()

    time.sleep(1)

    # Set font options to arial
    browser.find_element_by_xpath('//*[@id="delFontType"]/option[1]').click()

    time.sleep(1)

    # Set Search terms in bold type to true, if it is false
    if not browser.find_element_by_id('termBold').is_selected():
        browser.find_element_by_id('termBold').click()

    time.sleep(1)

    # Set Search terms underlined to false, if it is true
    if browser.find_element_by_id('termUnld').is_selected():
        browser.find_element_by_id('termUnld').click()

    time.sleep(1)

    # Set deliver in two columns to false, if it is true
    if browser.find_element_by_id('enhancedDelOption').is_selected():
        browser.find_element_by_id('enhancedDelOption').click()

    time.sleep(1)

    # Press download
    browser.find_element_by_xpath('//*[@id="deliv-dialogbox"]/form/div[2]/div/span[1]/a').click()


# END OF download FUNCTION

# def wait_by_id(browser, id, type):
#    try:
#        WebDriverWait(browser, 120).until(type((By.ID, id)))
#    except TimeoutException:
#        print('Could not locate ' + id + ' by id')
#        log_errors.write('Could not locate ' + id + ' by id\n')


# END OF wait_by_id FUNCTION

def wait_by_id(browser, elementid, ectype, errmsg):
    try:
        WebDriverWait(browser, 120).until(ectype((By.ID, elementid)))
    except TimeoutException:
        print(errmsg)
        log_errors.write(errmsg + '\n')
        browser.quit()
        sys.exit(1)


# END OF wait_by_id FUNCTION

# def wait_by_xpath(browser, xpath, type):
#    try:
#        WebDriverWait(browser, 120).until(type((By.XPATH, xpath)))
#    except TimeoutException:
#        print('Cold not locate ' + xpath + ' by xpath')
#       log_errors.write('Could not locate ' + xpath + ' by xpath\n')


# END OF wait_by_xpath FUNCTION

def wait_by_xpath(browser, xpath, ectype, errmsg):
    try:
        WebDriverWait(browser, 120).until(ectype((By.XPATH, xpath)))
    except TimeoutException:
        print(errmsg)
        log_errors.write(errmsg + '\n')
        browser.quit()
        sys.exit(1)

# END OF wait_by_xpath FUNCTION

def wait_random_time():
    seconds = 5 + (random.random() * 5)
    time.sleep(seconds)

    # END OF wait_random_time FUNCTION

def compare_dates(first_date, second_date):

    first_date_split = first_date.split('/')
    second_date_split = second_date.split('/')

    first_year = int(first_date_split[2])
    second_year = int(second_date_split[2])

    if first_year > second_year:
        return 1
    elif first_year < second_year:
        return -1

    first_month = int(first_date_split[0])
    second_month = int(second_date_split[0])

    if first_month > second_month:
        return 1
    elif first_month < second_month:
        return -1

    first_day = int(first_date_split[1])
    second_day = int(second_date_split[1])
    if first_day > second_day:
        return 1
    elif first_day < second_day:
       return -1

    return 0

# END OF compare_dates FUNCTION

def get_month_ending(date):

    date_split = date.split('/')
    month = int(date_split[0])
    year = int(date_split[2])
    new_date = ''
    if month == 1:
        new_date =  '0' + str(month) +'/31/' + str(year)
    elif month == 2:
        if year % 4 == 0:
            new_date = '0' + str(month) + '/29/' + str(year)
        else:
            new_date = '0' + str(month) + '/28/' + str(year)
    elif month == 3:
        new_date = '0' + str(month) + '/31/' + str(year)
    elif month == 4:
        new_date = '0' + str(month) + '/30/' + str(year)
    elif month == 5:
        new_date = '0' + str(month) + '/31/' + str(year)
    elif month == 6:
        new_date = '0' + str(month) + '/30/' + str(year)
    elif month == 7:
        new_date = '0' + str(month) + '/31/' + str(year)
    elif month == 8:
        new_date = '0' + str(month) + '/31/' + str(year)
    elif month == 9:
        new_date = '0' + str(month) + '/30/' + str(year)
    elif month == 10:
        new_date =  str(month) + '/31/' + str(year)
    elif month == 11:
        new_date = str(month) + '/30/' + str(year)
    elif month == 12:
        new_date = str(month) + '/31/' + str(year)

    return new_date
# END OF get_month_ending FUNCTION

def get_next_month_beginning(date):

    date_split = date.split('/')
    month = int(date_split[0])
    year = int(date_split[2])

    new_date = ''
    if month == 1:
        new_date = '0' + str(month + 1) + '/01/' + str(year)
    elif month == 2:
        new_date = '0' + str(month + 1) + '/01/' + str(year)
    elif month == 3:
        new_date = '0' + str(month + 1) + '/01/' + str(year)
    elif month == 4:
        new_date = '0' + str(month + 1) + '/01/' + str(year)
    elif month == 5:
        new_date = '0' + str(month + 1) + '/01/' + str(year)
    elif month == 6:
        new_date = '0' + str(month + 1) + '/01/' + str(year)
    elif month == 7:
        new_date = '0' + str(month + 1) + '/01/' + str(year)
    elif month == 8:
        new_date = '0' + str(month + 1) + '/01/' + str(year)
    elif month == 9:
        new_date = str(month + 1) + '/01/' + str(year)
    elif month == 10:
        new_date = str(month + 1) + '/01/' + str(year)
    elif month == 11:
        new_date = str(month + 1) + '/01/' + str(year)
    elif month == 12:
        new_date = '01/31/' + str(year + 1)

    return new_date
# END OF get_next_month_beginning FUNCTIOn