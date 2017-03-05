from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
import utils
import getpass
import time

# Set the path to chromedriver
path_to_chromedriver = 'res/chromedriver/chromedriver.exe'

# Create the browser with the given driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

print("---------------------------------LOG------------------------------------")
# Set the url and open it
url = 'http://uob-metalib.hosted.exlibrisgroup.com/V/?func=native-link&resource=BHM02155'
browser.get(url)

utils.wait_by_id(browser, 'j_submit', EC.element_to_be_clickable, "ERROR LOADING CANVAS PAGE: CHECK INTERNET CONNECTION?")

print("URL OPENED SUCCESSFULLY!")
print("CONFIGURATION PART")

# Store user and password
user = input('Please provide your uob id: ')
print(user)
print("ID provided!")
pwd = getpass.getpass('Please provide your uob password: ')
print(pwd)
print("Password provided!")

# Login to canvas
utils.canvaslogin(browser, user, pwd)

script_done = False
while not script_done:

    # Prompt for search term
    searchterm = input("Provide the search term:")
    print(searchterm)
    print("SEARCH TERM PROVIDED")
    searchconfig = 'company(' + searchterm + ' pre/3 #80plus#)'

    # Prompt for date
    print("Provide input for the starting date")
    valid = False
    fromDateMonth = "01"
    fromDateYear = "1996"
    fromDateDay = "01"
    while not valid:
        fromDateMonth = input('Please input a valid month in format MM. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not fromDateMonth:
            fromDateMonth = "01"
        valid = utils.checkmonth(fromDateMonth)

    valid = False
    while not valid:
        fromDateYear = input('Please input a valid year in format YYYY. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not fromDateYear:
            fromDateYear = "1996"
        valid = utils.checkyear(fromDateYear)

    valid = False
    while not valid:
        fromDateDay = input('Please input a valid day in format DD. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not fromDateDay:
            fromDateDay = "01"
        valid = utils.checkday(fromDateDay, fromDateMonth, fromDateYear)

    fromDate = fromDateMonth + "/" + fromDateDay + "/" + fromDateYear
    print(fromDate)
    print("Beginning date provided!")

    print("Provide input for the ending date")
    valid = False
    toDateMonth = "08"
    toDateYear = "2015"
    toDateDay = "31"
    while not valid:
        toDateMonth = input('Please input a valid month in format MM. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not toDateMonth:
            toDateMonth = "08"
        valid = utils.checkmonth(toDateMonth)

    valid = False
    while not valid:
        toDateYear = input('Please input a valid year in format YYYY. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not toDateYear:
            toDateYear = "2015"
        valid = utils.checkyear(toDateYear)

    valid = False
    while not valid:
        toDateDay = input('Please input a valid day in format DD. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not toDateDay:
            toDateDay = "31"
        valid = utils.checkday(toDateDay, toDateMonth, toDateYear)

    toDate = toDateMonth + "/" + toDateDay + "/" + toDateYear
    print(toDate)
    print("Ending date provided!")

    # Back to selenium

    fromDateAux = fromDate
    toDateAux = utils.get_month_ending(fromDateAux)

    while utils.compare_dates(toDateAux, toDate) != 1:

        # Go to news page
        utils.gotonews(browser)

        # Search the term on the page
        utils.searchpage(browser, searchconfig, fromDateAux, toDateAux)

        # Check if No Documents were found for the search

        utils.check_no_documents(browser)

        # Check if too many documents were found for the search

        utils.check_many_results(browser)


        # TODO - CREATE THE MAIN LOOP
        # TODO - CHANGE THE SEARCH TERMS
        # TODO - CREATE THE LOOP FOR MONTHS
        # TODO - CREATE THE LOOP FOR RESULTS

        utils.manage_download(browser)

        time.sleep(10)

        fromDateAux = utils.get_next_month_beginning(fromDateAux)
        toDateAux = utils.get_month_ending(fromDateAux)

    response = input("Search for another term? Prompt y for yes, anything else for no")

    if response == 'y':
        script_done = True

    utils.wait_random_time()

time.sleep(10)

browser.quit()