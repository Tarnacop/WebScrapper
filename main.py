import utils, getpass, time, os, shutil

from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC


utils.print_path_to_log()

path_to_downloads = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': path_to_downloads}
chrome_options.add_experimental_option('prefs', prefs)

# Set the path to chromedriver
path_to_chromedriver = 'res/chromedriver/chromedriver.exe'

# Create the browser with the given driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=chrome_options)

print("---------------------------------LOG------------------------------------")
utils.print_log("---------------------------------LOG------------------------------------")

# Set the url and open it
url = 'http://uob-metalib.hosted.exlibrisgroup.com/V/?func=native-link&resource=BHM02155'
browser.get(url)

utils.wait_by_id(browser, 'j_submit', EC.element_to_be_clickable, "ERROR LOADING CANVAS PAGE: CHECK INTERNET CONNECTION")

print("URL OPENED SUCCESSFULLY")
print("CONFIGURATION PART")

# Store user and password
user = input('PROVIDE YOUR UOB ID: ')
print(user)
print("ID PROVIDED")
pwd = getpass.getpass('PROVIDE YOUR UOB PASSWORD: ')
print(pwd)
print("PASSWORD PROVIDED")

# Login to canvas
utils.canvaslogin(browser, user, pwd)

script_done = False
while not script_done:

    # Prompt for search term
    searchterm = input("PROVIDE THE SEARCH TERM: ")
    print(searchterm)
    utils.print_log(searchterm)
    print("SEARCH TERM PROVIDED")
    searchconfig = 'company(' + searchterm + ' pre/3 #80plus#)'

    # Prompt for date
    print("PROVIDE INPUT FOR THE STARTING DATE")
    valid = False
    fromDateMonth = "01"
    fromDateYear = "1996"
    fromDateDay = "01"
    while not valid:
        fromDateMonth = input('INPUT A VALID MONTH IN THE FORMAT MM. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not fromDateMonth:
            fromDateMonth = "01"
        valid = utils.checkmonth(fromDateMonth)

    valid = False
    while not valid:
        fromDateYear = input('INPUT A VALID YEAR IN THE FORMAT YYYY. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not fromDateYear:
            fromDateYear = "1996"
        valid = utils.checkyear(fromDateYear)

    valid = False
    while not valid:
        fromDateDay = input('INPUT A VALID YEAR IN THE FORMAT DD. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not fromDateDay:
            fromDateDay = "01"
        valid = utils.checkday(fromDateDay, fromDateMonth, fromDateYear)

    fromDate = fromDateMonth + "/" + fromDateDay + "/" + fromDateYear
    print(fromDate)
    utils.print_log("FROM DATE" + " " + fromDate)
    print("FROM DATE PROVIDED")

    print("PROVIDE INPUT FOR THE ENDING DATE")
    valid = False
    toDateMonth = "08"
    toDateYear = "2015"
    toDateDay = "31"
    while not valid:
        toDateMonth = input('INPUT A VALID MONTH IN THE FORMAT MM. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not toDateMonth:
            toDateMonth = "08"
        valid = utils.checkmonth(toDateMonth)

    valid = False
    while not valid:
        toDateYear = input('INPUT A VALID YEAR IN THE FORMAT YYYY. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not toDateYear:
            toDateYear = "2015"
        valid = utils.checkyear(toDateYear)

    valid = False
    while not valid:
        toDateDay = input('INPUT A VALID DATE IN THE FORMAT DD. PRESS ENTER IF YOU WANT THE DEFAULT VALUE:')
        if not toDateDay:
            toDateDay = "31"
        valid = utils.checkday(toDateDay, toDateMonth, toDateYear)

    toDate = toDateMonth + "/" + toDateDay + "/" + toDateYear
    print(toDate)
    utils.print_log("TO DATE" + " " + toDate)
    print("END DATE PROVIDED")
    print("END OF CONFIG PART")
    # Back to selenium

    fromDateAux = fromDate
    toDateAux = utils.get_month_ending(fromDateAux)

    os.mkdir(os.path.join(path_to_downloads, searchterm))
    while utils.compare_dates(toDateAux, toDate) != 1:

        print("FROM: " + fromDateAux + " TO: " + toDateAux)
        utils.print_log("FROM: " + fromDateAux + " TO: " + toDateAux)

        # Go to news page
        utils.gotonews(browser)

        # Search the term on the page
        utils.searchpage(browser, searchconfig, fromDateAux, toDateAux)

        # Check if No Documents were found for the search

        utils.check_no_documents(browser)

        # Check if too many documents were found for the search

        utils.check_many_results(browser)

        utils.manage_download(browser)

        time.sleep(10)


        files = os.listdir(path_to_downloads)
        for f in files:
            if ".RTF" not in f:
                continue
            src = os.path.join(path_to_downloads, f)
            dst = os.path.join(path_to_downloads, searchterm, f)
            shutil.move(src, dst)

        fromDateAux = utils.get_next_month_beginning(fromDateAux)
        toDateAux = utils.get_month_ending(fromDateAux)
    utils.print_log("------------------------------------------------------------------------")
    response = input("SEARCH FOR ANOTHER TERM? PROMPT y FOR YES, ANYTHING ELSE FOR NO")

    if response == 'y':
        script_done = True

    utils.wait_random_time()

time.sleep(10)

browser.quit()