###############################################################################################
#
# DATE:         6/18/2018
# AUTHOR:       Lila Fata
# FILE:         automateBrowseQAReq.py
# DESCRIPTION:  This script file contains methods (two ways) to automate the
#               browsing of QA Engineer, Automation requisition (0094391) from
#               Conversant Media
#
# NOTES:        Here are the assumptions/instructions to run this script -
#               1) This program was executed using IDLE Python 3.7 Shell on
#                  a Windows 10 laptop
#               2) Install selenium at Command Prompt with following input:
#                  'pip install selenium'
#               3) Download chromedriver latest version (2.40 chromedriver_win32.zip) from
#                  https://sites.google.com/a/chromium.org/chromedriver/downloads
#               4) Copy chromedriver application from zipped folder 'chromedriver_win32' to
#                  the same directory location of this script 'automateBrowseQAReq.py'
#
###############################################################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#
# First way to browse QA requisition 0094391
# - Follow the steps given in the example given in QA - Test Instructions
#
def firstWayBrowseQAReq():
    print("Automating 1st way of browsing QA requisition (0094391)...")
    try:
        driver = webdriver.Chrome() #Open chrome browser
        driver.get("https://conversantmedia.com")  # Navigate to conversantmedia.com and click on 'Careers'
        driver.find_element_by_xpath("""//*[@id="hs_menu_wrapper_module_13884994340213"]/ul/li[6]/a""").click()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_xpath("""//*[@id="cnvrTrack"]""").click() # Click on 'Join our team'
        driver.switch_to_window(driver.window_handles[1])  # Switch to new tab
        searchEntry = driver.find_element_by_id("search-query-input") # Go to 'SEARCH ALL OPENINGS...'
        searchEntry.send_keys("0094391" + Keys.ENTER) # Input req 0094391 and click on QA Engineer, Automation
        time.sleep(2)
        searchEntry.find_element_by_xpath("""//*[@id="search-container"]/div[5]/div/a""").click()
        time.sleep(15)
        driver.quit()
        print("\nSuccess: 1st way to browse QA requisition\n")            
        return True
    except:
        print("\nException: 1st way to browse QA requisition!\n")
        driver.quit()
        return False

#
# Second way to browse QA requisition 0094391
# - Navigate directly to this job requisition number
#
def secondWayBrowseQAReq():
    print("Automating 2nd way of browsing QA requisition (0094391)...")
    try:
        driver = webdriver.Chrome()
        driver.get("http://jobs.conversantmedia.com/#/search?query=0094391")
        driver.find_element_by_xpath("""//*[@id="search-container"]/div[5]/div/a""").click()
        time.sleep(15)
        driver.quit()
        print("\nSuccess: 2nd way to browse QA requisition\n")        
        return True
    except:
        print("\nException: 2nd way to browse QA requisition!\n")
        driver.quit()
        return False            

#
# Main function to automate as many ways (two ways) possible to browse QA requision 0094391
#
def main():
    browse1 = False
    browse2 = False
    if (firstWayBrowseQAReq()):
        browse1 = True
    if (secondWayBrowseQAReq()):
        browse2 = True
    if (browse1 and browse2):
        print("\nAll methods to Browse QA Req (0094391) successful\n")
    else:
        print("\nOne or more methods to Browse QA Req (0094391) failed\n")

if __name__ == "__main__":
    main()
